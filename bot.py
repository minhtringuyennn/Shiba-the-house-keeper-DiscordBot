#!/usr/bin/python3
import asyncio
import datetime
import random
import configparser
from random import randint
import discord
from discord.ext import commands

read_config = configparser.ConfigParser()
read_config.read("./config/default_config.ini")
TOKEN = read_config.get("config", "Token")
PREFIX = read_config.get("config", "CommandPrefix")


intents = discord.Intents().all()
client = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

#Check if bot deploy successfully
@client.event
async def on_ready():
    print("Bot is up!")

#Only certain role can participate
#@commands.has_role("Dân chơi")

#Main def
@client.command()

async def roll(ctx, *, input="5"):
    #Init
    if (input.isnumeric() == 0):
        await ctx.send(f"Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        return

    seconds = int(input)
    if seconds <= 0:
        seconds = int(5)
    seconds = max(seconds, 5)
    seconds = min(seconds,90)

    #First Message
    embed = discord.Embed(title="Ai là người tiếp theo?!", color=ctx.author.color)
    hours = 7
    calc = datetime.datetime.now() + datetime.timedelta(seconds) + datetime.timedelta(hours = hours)
    end = calc.strftime("%X")
    embed.add_field(name="Kết thúc vào: ", value=f"{end}")
    embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
    my_msg = await ctx.send(embed=embed)
    await my_msg.add_reaction(":amongus_VOTED:764909622754017322>")

    #Waiting
    while (seconds > 0):
        if (seconds > 5):
            await asyncio.sleep(5)
            seconds = seconds - 5
        else:
            await asyncio.sleep(1)
            seconds = seconds - 1
        embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
        await my_msg.edit(embed=embed)

    #Get data
    new_msg = await ctx.channel.fetch_message(my_msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    #Second message
    if len(users) != 0:
        chosen = random.choice(users)
        embed.set_footer(text=f'Người lên thớt tiếp theo chính là {chosen.name}')
        await my_msg.edit(embed=embed)
        await ctx.send(f"Ỏ, tới bạn kìa {chosen.mention} <:meow_woah:759037054968397904>")
    else:
        embed.set_footer(text='Không tìm thấy người may mắn tiếp theo. 404 Not Found!!!')
        await my_msg.edit(embed=embed)
        await ctx.send("Không vote sao tôi random đây hả mấy ba? <:voli:784077759001526272>")


#Second def
@client.command()
async def rollroom(ctx, *, input="5"):
    #Init
    if (input.isnumeric() == 0):
        await ctx.send(f"Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        return

    seconds = int(input)
    if seconds <= 0:
        seconds = int(5)
    seconds = max(seconds, 5)
    seconds = min(seconds,90)

    #Check
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("Bạn chưa kết nối đến channel!")
        return

    #First Message
    embed = discord.Embed(title="Ai là người tiếp theo?!", color=ctx.author.color)
    hours = 7
    calc = datetime.datetime.now() + datetime.timedelta(seconds) + datetime.timedelta(hours = hours)
    end = calc.strftime("%X")
    embed.add_field(name="Kết thúc vào: ", value=f"{end}")
    embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
    my_msg = await ctx.send(embed=embed)

    #Get data
    #channel = ctx.message.author.voice.channel
    members = channel.members
    users = [] #(list)
    for member in members:
        if not member.bot:
            users.append(member)
        
    #Waiting
    while (seconds > 0):
        if (seconds > 5):
            await asyncio.sleep(5)
            seconds = seconds - 5
        else:
            await asyncio.sleep(1)
            seconds = seconds - 1
        embed.set_footer(text=f"Kết thúc trong {seconds} giây nữa!")
        await my_msg.edit(embed=embed)

    #Second message
    if len(users) != 0:
        chosen = random.choice(users)
        embed.set_footer(text=f'Người lên thớt tiếp theo chính là {chosen.name}')
        await my_msg.edit(embed=embed)
        await ctx.send(f"Ỏ, tới bạn kìa {chosen.mention} <:meow_woah:759037054968397904>")
    else:
        embed.set_footer(text='Không tìm thấy người may mắn tiếp theo. 404 Not Found!!!')
        await my_msg.edit(embed=embed)
        await ctx.send("Không vote sao tôi random đây hả mấy ba? <:voli:784077759001526272>")

#Third def
@client.command()    
async def listroom(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("Bạn chưa kết nối đến channel!")
        return

    #Print Menu
    embed = discord.Embed(title="Danh sách những người đang chơi ToD đâyy <:meow_woah:759037054968397904>", color=ctx.author.color)

    #Get data
    #channel = ctx.message.author.voice.channel
    members = channel.members
    getChannelName = ctx.author.voice.channel
    usr = []
    for member in members:
        if not member.bot:
            usr.append(member.name)

    #Print Message
    embed.add_field(name=f"Những người trong {getChannelName} gồm có: ", value=f"{', '.join([i for i in usr])}", inline=False)
    embed.set_footer(text="Người may mắn tiếp theo sẽ là ai đây???")
    await ctx.send(embed=embed)

#Fourth def
@client.command()
async def remainTurn(ctx, mininput = "1", maxinput = "10" ):
    #Init
    if mininput.isnumeric() == 0 or maxinput.isnumeric() == 0 or int(mininput) > int(maxinput) or int(maxinput) > 21 or int(mininput) < 1:
        await ctx.send(f"Chỉ nhập giá trị từ 1 đến 20 <:frog_noo:759037055036031007>")
        return

    #Calc
    mininput = int(mininput)
    maxinput = int(maxinput)
    turn = randint(mininput, maxinput)

    #Return result
    await  ctx.send(f"Hãy chơi thêm {turn} lượt nữa!")

#Help def
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        coulour = discord.Color.red()
    )
    embed.set_author(name='Thông tin nhanh:')
    embed.add_field(name='Về bot', value='Tác giả: Bạch Ngọc Minh Tâm và Nguyễn Minh Trí \n Một bot đơn giản để phục vụ trò chơi Truth or Dare cho nhóm bạn của tác giả.', inline=True)
    embed.add_field(name='>roll', value='Có 2 kiểu: " >roll " với mặc định là 5s và " >roll {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.', inline=False)
    embed.add_field(name='>rollroom', value='Có 2 kiểu: " >rollroom " với mặc định là 5s và " >rollroom {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.', inline=False)
    embed.add_field(name='>listroom', value='Trả về thông tin channel hiện tại mà người chơi đang tham gia.', inline=False)
    embed.add_field(name='>remainTurn', value='Có 2 kiểu: " >remainTurn " và " >remainTurn {số lượt ít nhất} {số lượt nhiều nhất} " \n "Trả về số lượt chơi còn lại của trò chơi \n Giá trị trả về ít nhất 1 lượt chơi và tối đa 20 lượt chơi.', inline=False)
    # await author.send(embed=embed)
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Tưởng rằng lệnh sẽ được thực thi sao??? Không! Đây là Dio <:jco:781338022078840832>")
        return
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Nhập sai lệnh rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        await ctx.send(f"Các lệnh bot hỗ trợ:")
        await help(ctx)
        return

client.run(TOKEN)