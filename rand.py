import discord
from discord.ext import commands
import random
import asyncio
import datetime
import string
import voice

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def roll(self,ctx, *, input="5"):
        # Init
        if (input.isnumeric() == 0):
            await ctx.send(f"Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
            return
        seconds = int(input)
        if seconds <= 0:
            seconds = int(5)
        seconds = max(seconds, 5)
        seconds = min(seconds, 90)
        # First Message
        embed = discord.Embed(title="Ai là người tiếp theo?!", color=ctx.author.color)
        hours = 7
        calc = datetime.datetime.now() + datetime.timedelta(seconds) + datetime.timedelta(hours=hours)
        end = calc.strftime("%X")
        embed.add_field(name="Kết thúc vào: ", value=f"{end}")
        embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
        my_msg = await ctx.send(embed=embed)
        await my_msg.add_reaction(":amongus_VOTED:764909622754017322>")
        
        # Waiting
        while (seconds > 0):
            if (seconds > 5):
                await asyncio.sleep(5)
                seconds = seconds - 5
            else:
                await asyncio.sleep(1)
                seconds = seconds - 1
            embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
            await my_msg.edit(embed=embed)

        # Get data
        new_msg = await ctx.channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        # Second message
        if len(users) != 0:
            chosen = random.choice(users)
            embed.set_footer(text=f'Người lên thớt tiếp theo chính là {chosen.name}')
            await my_msg.edit(embed=embed)
            await ctx.send(f"Ỏ, tới bạn kìa {chosen.mention} <:meow_woah:759037054968397904>")
        else:
            embed.set_footer(text='Không tìm thấy người may mắn tiếp theo. 404 Not Found!!!')
            await my_msg.edit(embed=embed)
            await ctx.send("Không vote sao tôi random đây hả mấy ba? <:voli:784077759001526272>")

    @commands.command()
    async def listroom(self,ctx):
        room = None
        # Print Menu
        if ctx.author.voice and ctx.author.voice.channel:
            room = voice.VoiceRoom(ctx)
        else:
            await ctx.send("Không join room kêu list room ra kiểu gì ba? <:voli:784077759001526272>")
            return
        embed = discord.Embed(title="Danh sách những người đang chơi ToD đâyy <:meow_woah:759037054968397904>",
                                color=ctx.author.color)
        # Get data
        # channel = ctx.message.author.voice.channel
        getChannelName = room.channelname(ctx)
        # Print Message
        members = room.listname()
        embed.add_field(name=f"Những người trong {getChannelName} gồm có: ", value=f"{', '.join([i for i in members])}",
                        inline=False)
        embed.set_footer(text="Người may mắn tiếp theo sẽ là ai đây???")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def rollroom(self, ctx, *, input="1"):
        random.seed(datetime.datetime.now())
        
        # Init
        if (input.isnumeric() == 0):
            await ctx.send("Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
            return

        seconds = int(input)
        if seconds <= 0:
            seconds = int(1)
        seconds = max(seconds, 1)
        seconds = min(seconds, 90)
        # Check
        if ctx.author.voice and ctx.author.voice.channel:
            room = voice.VoiceRoom(ctx)
        else:
            await ctx.send("Bạn chưa kết nối đến channel!")
            return

        # First Message
        embed = discord.Embed(title="Ai là người tiếp theo?!", color=ctx.author.color)
        hours = 7
        calc = datetime.datetime.now() + datetime.timedelta(seconds) + datetime.timedelta(hours=hours)
        end = calc.strftime("%X")
        embed.add_field(name="Kết thúc vào: ", value=f"{end}")
        embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
        my_msg = await ctx.send(embed=embed)

        # Waiting
        while (seconds > 0):
            await asyncio.sleep(1)
            seconds = seconds - 1
            embed.set_footer(text=f'Kết thúc trong {seconds} giây nữa!')
            await my_msg.edit(embed=embed)

        room.refresh(ctx)
        members = room.members

        # Second message
        if len(members) >= 2:
            #Prevent repeat
            chosen = random.choice(members)
            while chosen == ctx.author:
                chosen = random.choice(members)

            embed.set_footer(text=f'Người lên thớt tiếp theo chính là {chosen.name}')
            await my_msg.edit(embed=embed)
            await ctx.send(f'Ỏ, tới bạn kìa {chosen.mention} <:pikachu_smile:767261524879867914>')
        else:
            embed.set_footer(text='Không tìm thấy người may mắn tiếp theo. 404 Not Found!!!')
            await my_msg.edit(embed=embed)
            await ctx.send("Ủa đâu mất tiêu hết rồi mấy ba? <:meo_chmuahme:772813299251150849>")
        
    @commands.command()
    async def choose(self, ctx, *, input=""):
        if input == "":
            await ctx.send(f"Nhập vào đàng hoàng coi <:meow_glance:758735706360774666>")
            return

        sz = len(input)
        author = ctx.message.author
        list = input.split(", ")
        value = random.choice(list)

        if len(list) == 1 and sz > 1 or "" in list:
            await ctx.send(f"Tính exploit gì đây <:meow_glance:758735706360774666>")
            return

        if len(list) == 1:
            await ctx.send(f"Có đáp án rõ ràng thế lại còn gì hả {author.mention} <:meow_glance:758735706360774666>")
            return
        await ctx.send(f"Tôi chọn `{value}` nhé {author.mention} <:meow_huh:759037054725128242>")

    @commands.command()
    async def remainTurn(ctx, mininput="1", maxinput="10"):
        # Init
        if mininput.isnumeric() == 0 or maxinput.isnumeric() == 0 or int(mininput) > int(maxinput) or int(
                maxinput) > 21 or int(mininput) < 1:
            await ctx.send(f"Nhập vào không đúng (chỉ từ 1 đến 20) hoặc nhập dữ liệu sai <:frog_noo:759037055036031007>")
            return

        # Calc
        mininput = int(mininput)
        maxinput = int(maxinput)
        turn = random.randint(mininput, maxinput)
        # Return result
        await  ctx.send(f"Hãy chơi thêm {turn} lượt nữa!")
