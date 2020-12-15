#!/usr/bin/python3
import asyncio
import datetime
import random
import configparser
from random import randint
import discord
from discord.ext import commands
from discord.utils import get
# import youtube_dl
import string
import os
import re
import emoji

read_config = configparser.ConfigParser()
read_config.read("./config/config.ini")
TOKEN = read_config.get("config", "Token")
PREFIX = read_config.get("config", "CommandPrefix")

intents = discord.Intents().all()
client = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Check if bot deploy successfully
@client.event
async def on_ready():
    print("Bot is up!")

# Only certain role can participate
# @commands.has_role("Dân chơi")

# Main def
@client.command()
async def roll(ctx, *, input="5"):
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
    users.pop(users.index(client.user))

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

# Second def
@client.command()
async def rollroom(ctx, *, input="5"):
    # Init
    if (input.isnumeric() == 0):
        await ctx.send(f"Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        return

    seconds = int(input)
    if seconds <= 0:
        seconds = int(5)
    seconds = max(seconds, 5)
    seconds = min(seconds, 90)

    # Check
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
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

    # Get data
    members = channel.members
    users = []  # (list)
    for member in members:
        if not member.bot:
            users.append(member)
        
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

# Third def
@client.command()
async def listroom(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("Bạn chưa kết nối đến channel!")
        return

    # Print Menu
    embed = discord.Embed(title="Danh sách những người đang chơi ToD đâyy <:meow_woah:759037054968397904>",
                          color=ctx.author.color)

    # Get data
    # channel = ctx.message.author.voice.channel
    members = channel.members
    getChannelName = ctx.author.voice.channel
    usr = []
    for member in members:
        if not member.bot:
            usr.append(member.name)

    # Print Message
    embed.add_field(name=f"Những người trong {getChannelName} gồm có: ", value=f"{', '.join([i for i in usr])}",
                    inline=False)
    embed.set_footer(text="Người may mắn tiếp theo sẽ là ai đây???")
    await ctx.send(embed=embed)

# Fourth def
@client.command()
async def remainTurn(ctx, mininput="1", maxinput="10"):
    # Init
    if mininput.isnumeric() == 0 or maxinput.isnumeric() == 0 or int(mininput) > int(maxinput) or int(
            maxinput) > 21 or int(mininput) < 1:
        await ctx.send(f"Nhập vào không đúng (chỉ từ 1 đến 20) hoặc nhập dữ liệu sai <:frog_noo:759037055036031007>")
        return

    # Calc
    mininput = int(mininput)
    maxinput = int(maxinput)
    turn = randint(mininput, maxinput)

    # Return result
    await  ctx.send(f"Hãy chơi thêm {turn} lượt nữa!")

# Fifth def

@client.command()
async def choose(ctx, *, input=""):
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

# # Youtube streaming
# players = {}

# @client.command(pass_context=True)
# async def leave(ctx):
#     guild = ctx.message.guild
#     voice_client = guild.voice_client
#     await voice_client.disconnect()

# @client.command(name='p', invoke_without_subcommand=True)
# async def p(ctx):
#     destination = ctx.author.voice.channel
#     if ctx.voice_state.voice:
#         await ctx.voice_state.voice.move_to(destination)
#         return
    
#     ctx.voice_state.voice = await destination.connect()
#     await ctx.send(f"Joined {ctx.author.voice.channel} Voice Channel")
#     # Return music
#     guild = ctx.message.guild
#     voice_client = guild.voice_client
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()

# Add react def

@client.command()
async def createvote(ctx,*, id = ""):
    
    if (id == ""):
        logs =  await ctx.channel.history(limit=1).flatten()
        msg = logs[0]
    else:
        try:
            msg = await ctx.channel.fetch_message(id)
        except:
            await ctx.send(f"Nhập không hợp lệ òi, Đâu thấy tin nhắn nào có ID đó đâu <:wut:781338137985155113><:voli:784077759001526272>")
            return
    await ctx.message.delete()
    list = msg.content.split("\n")
    for lt in list:
        lookup = ""
        server_match = re.search(r'<a?:(\w+):(\d+)>', lt)
        custom_match = re.search(r':(\w+):', lt)
        if server_match:
            lookup = server_match.group(1)
            await msg.add_reaction(get(ctx.message.guild.emojis, name=lookup))
        elif custom_match:
            lookup = custom_match.group(1)  
            await msg.add_reaction(get(ctx.message.guild.emojis, name=lookup))
        else:
            for emj in lt.split(' '):
                if emj in emoji.UNICODE_EMOJI:
                    await msg.add_reaction(emj)
    try:
        await msg.remove_reaction("<:amongus_VOTED:764909622754017322>",client.user)
    except:
        return

# Mocking Text Generator
@client.command()
async def mock(ctx, *, input= ""): 
    output = ""
    for char in input: 
        if char.isalpha(): 
            if random.choice([True, False]): 
                output += char.upper()
            else: 
                output += char.lower()
        else: 
            output += char 

    if output == "":
        output = ctx.author.name  
        temp = ""
        for char in output: 
            if char.isalpha(): 
                if random.choice([True, False]): 
                    temp += char.upper()
                else: 
                    temp += char.lower()
            else: 
                temp += char
            output = temp
    
    await ctx.send(f"{output}")

    #send nud...gif
    embed = discord.Embed()
    embed.set_image(url='https://cdn.discordapp.com/attachments/775431017053945868/787667035580530728/minhtringu-ran-this-command.gif')
    await ctx.send(embed=embed)

#Shouting to someone
@client.command()
async def shout(ctx, *, input= ""): 
    output = ""
    
    for char in input: 
        if char.isalpha(): 
            if char.islower(): 
                output += char.upper()
            else: 
                output += char
        else: 
            output += char

    if output != "":
        l = 1
        while l < 5:
            if input[len(input)-1].isalpha():
                output += input[len(input)-1].upper()
            l += 1
        while l < 10:
            output += "!"
            l+=1
        await ctx.send(f"{output}")
    else:
        await ctx.send(f"ARGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

    #send nud...gif
    embed = discord.Embed()
    embed.set_image(url='https://media1.tenor.com/images/9b29ee560a03a7441490e95778922aaa/tenor.gif')
    await ctx.send(embed=embed)

#OwO what's this
@client.command()
async def owo(ctx):
    await ctx.send("OwO")

@client.command()
async def OwO(ctx):
    await ctx.send("OwO")

#etou...
@client.command()
async def etou(ctx, *, input = ""):
    if input == "":
        await ctx.send("etou... 👉👈")
    else:
        await ctx.send(f"{input}... 👉👈")

#how long is your dick?
@client.command()
async def penis(ctx, *, name=""):
    l = 0
    penis = "8D"
    s = randint(0, 15)
    
    while l<s:
        penis = penis[:1] + '=' + penis[1:]
        l+=1

    if len(name) == 0:
        name = "your"
    if len(penis)<5:
        await ctx.send(f"get rekt kid, {name} dick is just this {penis} long <:meow_lovelybutt:759037054507810838>")
    elif len(penis)>12:
        name = name[0].upper() + name[1:]
        await ctx.send(f"WOW! {name} is this {penis} long! <:pepe_jesuschrist:758735706267844650>")
    else:
        name = name[0].upper() + name[1:]
        await ctx.send(f"{name} dick is this {penis} long")

#simp rate?
@client.command()
async def simprate(ctx, *, name=""):
    rate = randint(0, 100)
    tobe = "is"
    
    if len(name) == 0:
        name = "you"
        tobe = "are"

    if rate<15:
        await ctx.send(f"Ah I see, just {rate}%. {name} {tobe} the man of culture as well. <:hutthuoc:779543902617206804>")
    elif rate>80:
        name = name[0].upper() + name[1:]

        await ctx.send(f"WOW! {rate}%! {name} {tobe} such a simp! <:pepe_jesuschrist:758735706267844650>")
    else:
        name = name[0].upper() + name[1:]
        await ctx.send(f"{name} {tobe} {rate}% simp")

# Help def
@client.command(pass_context=True)
async def help(ctx):
    # author = ctx.message.author
    embed = discord.Embed(
        coulour=discord.Color.red()
    )
    embed.set_author(name='Thông tin nhanh:')
    embed.add_field(name='Về bot',
                    value='Tác giả: Bạch Ngọc Minh Tâm và Nguyễn Minh Trí \n Một bot đơn giản để phục vụ server cho nhóm bạn của tác giả.',
                    inline=True)
    embed.add_field(name='>roll',
                    value='Có 2 kiểu: " >roll " với mặc định là 5s và " >roll {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.',
                    inline=False)
    embed.add_field(name='>rollroom',
                    value='Có 2 kiểu: " >rollroom " với mặc định là 5s và " >rollroom {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.',
                    inline=False)
    embed.add_field(name='>listroom', value='Trả về thông tin channel hiện tại mà người chơi đang tham gia.',
                    inline=False)
    embed.add_field(name='>remainTurn',
                    value='Có 2 kiểu: " >remainTurn " và " >remainTurn {số lượt ít nhất} {số lượt nhiều nhất} " \n Trả về số lượt chơi còn lại của trò chơi \n Giá trị trả về ít nhất 1 lượt chơi và tối đa 20 lượt chơi.',
                    inline=False)
    embed.add_field(name='>choose',
                    value='Chỉ cần gõ " >choose {danh sách lựa chọn ngăn cách bởi dấu phẩy}"" \n Trả về sự lựa chọn ngẫu nhiên \n Có thể trả về dù chỉ với 1 hay rất nhiều lựa chọn',
                    inline=False)
    # embed.add_field(name='>p',
    #                 value='Chỉ cần gõ " >p {đường link Youtube}"" \n Join channel và phát nhạc cho mọi người \n Khi không cần thiết có thể gõ >leave \n Tính năng đang được xây dựng',
    #                 inline=False)
    embed.add_field(name='>mock',
                    value='Có 2 kiểu: " >mock " và " >mock {nội dung} " \n "Trả về Câu CHữ KHIÊu khícH \n Giá trị mặc định là tên người gọi lệnh.',
                    inline=False)
    embed.add_field(name='>shout',
                    value='Có 2 kiểu: " >shout " và " >shout {nội dung} " \n "Dùng để chửi thằng lợn nào đó \n Giá trị mặc định là ARGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH.',
                    inline=False)
    embed.add_field(name='>owo',
                    value='owo what is this',
                    inline=False)
    embed.add_field(name='>etou',
                    value='Có 2 kiểu: " >etou " và " >etou {nội dung} " \n :point_right::point_left:',
                    inline=False)
    embed.add_field(name='>penis',
                    value='Có 2 kiểu: " >penis " và " >penis {người được tag} " \n How long is yours? <:cuoi_deu:772700153806716928>',
                    inline=False)
    embed.add_field(name='>simprate',
                    value='Có 2 kiểu: " >simprate " và " >simprate {người được tag} " \n Bạn yêu người yêu bạn thế nào <:meow_woah:759037054968397904>',
                    inline=False)    
    embed.add_field(name='>createvote',
                    value='Có 2 kiểu: " >createvote " sẽ add emoji ở tin nhắn gần đó nhất và " >createvote {message id} "',
                    inline=False)
    # await author.send(embed=embed)
    await ctx.send(embed=embed)

# Get out of reach
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Tưởng rằng lệnh sẽ được thực thi sao??? Không! Đây là Dio <:jco:781338022078840832>")
        return    
    if isinstance(error, commands.BadArgument):
        await ctx.send(f"Nhập không hợp lệ rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        return    
    if isinstance(error, commands.MessageNotFound):
        await ctx.send(f"Nhập không hợp lệ òi, Đâu thấy tin nhắn nào có ID đó đâu <:wut:781338137985155113><:voli:784077759001526272>")
        return
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Nhập sai lệnh rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        await ctx.send(f"Các lệnh mà bot hỗ trợ:")
        await help(ctx)
        return

client.run(TOKEN)