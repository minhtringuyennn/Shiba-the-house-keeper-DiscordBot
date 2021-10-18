import discord
from discord.ext import commands
from discord.ext import tasks
from random import randint
import random
import praw
import configparser
import os
from PIL import Image, ImageDraw, ImageFont

PATH = "/root/Shiba-the-house-keeper/"

read_config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
read_config.read(path)
REDDITID = read_config.get("config", "redditCilentID")
REDDITSECRET = read_config.get("config", "redditSecretKey")
reddit = praw.Reddit(client_id = REDDITID,
                     client_secret= REDDITSECRET,
                     user_agent= "github - minhtringuyennn")

class Funny(commands.Cog):
    #OwO what's this
    @commands.command()
    async def mock(self, ctx, *, input= ""):
        await ctx.message.delete()
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
    @commands.command()
    async def shout(self,ctx, *, input= ""):
        await ctx.message.delete()
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
        await ctx.send(f"- _{ctx.message.author.name}_")
        #send nud...gif
        embed = discord.Embed()
        embed.set_image(url='https://media1.tenor.com/images/9b29ee560a03a7441490e95778922aaa/tenor.gif')
        await ctx.send(embed=embed)

    @commands.command()
    async def owo(self, ctx):
        await ctx.message.delete()
        await ctx.send("**OwO**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    @commands.command()
    async def OwO(self, ctx):
        await ctx.message.delete()
        await ctx.send("**OwO**")
        await ctx.send(f"- _{ctx.message.author.name}_")
    
    @commands.command()
    async def UwU(self, ctx):
        await ctx.message.delete()
        await ctx.send("**UwU**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    @commands.command()
    async def uwu(self, ctx):
        await ctx.message.delete()
        await ctx.send("**uwu**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    #etou...
    @commands.command()
    async def etou(self, ctx, *, input = ""):
        await ctx.message.delete()
        if input == "":
            await ctx.send("etou... 👉👈")
        else:
            await ctx.send(f"{input}... 👉👈")
        await ctx.send(f"- _{ctx.message.author.name}_")
        
    #how long is your dick?
    @commands.command()
    async def penis(self,ctx, *, name=""):
        l = 0
        penis = "8D"
        s = randint(0, 15)
        if (ctx.message.author.id == 443116194275524619 and name == ""):
            s = 15
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
    @commands.command()
    async def simprate(self,ctx, *, name=""):
        rate = randint(0, 100)
        realsimp =  [340643391618547712]
        if (ctx.message.author.id in realsimp):
            rate = randint(90, 100)
        for id in realsimp:
            if (str(id) in ctx.message.content):
                rate = randint(90, 100)
                break
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

    @commands.command()
    async def meme(self, ctx):
        # await ctx.message.delete()
        await ctx.send("Hể í yỏu mêm <:meo_phecan:772700153806716928>")

        communities_list = ["memes", "dankmemes"]
        commuinity = random.choice(communities_list)
        post_to_pick = random.randint(1, 50)
        
        _submissions = reddit.subreddit(commuinity).hot()
        submission = _submissions

        # https://i. -> image, v -> video
        while str(submission.url)[8] != 'i':
            for i in range(0, post_to_pick):
                submission = next(x for x in _submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command()
    async def mademeuwu(self, ctx):
        # await ctx.message.delete()
        await ctx.send("Nè, vui lên đi, bitch <:meow_lovelybutt:759037054507810838>")

        communities_list = ["aww", "wholesomegifs", "Eyebleach"]
        commuinity = random.choice(communities_list)
        post_to_pick = random.randint(1, 50)
        
        _submissions = reddit.subreddit(commuinity).hot()
        submission = _submissions

        # https://i. -> image, v -> video
        while str(submission.url)[8] != 'i':
            for i in range(0, post_to_pick):
                submission = next(x for x in _submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(aliases=['ponk', 'bonk'])
    async def pong(self, ctx, *, name = ""):
        # await ctx.message.delete()
        
        base = Image.open(PATH + "meme_img/bonk.png").convert("RGBA")
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(PATH + "Montserrat.ttf", 50)
        
        if len(name) == 0:
            tag_name = ctx.message.author.name
            author_name = "Shiba Bot"
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick
            author_name = ctx.message.author.nick
        else:
            tag_name = name
            author_name = ctx.message.author.nick
            
        author = ImageDraw.Draw(txt)
        author.text((30, 500), author_name, font=fnt, fill=(0, 0, 0, 255))
        
        tag = ImageDraw.Draw(txt)
        tag.text((450, 20), tag_name, font=fnt, fill=(0, 0, 0, 255))

        out = Image.alpha_composite(base, txt)
        out.save('bonk.png')
        
        await ctx.send(file=discord.File('bonk.png'))

    @commands.command(aliases=['luv', 'sendluv'])
    async def luvu(self, ctx, *, name = ""):
        await ctx.message.delete()
        
        base = Image.open(PATH + "meme_img/luv.jpg").convert("RGBA")
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(PATH + "Montserrat.ttf", 50)
        fnt2 = ImageFont.truetype(PATH + "Montserrat.ttf", 20)
        
        if len(name) == 0:
            tag_name = ctx.message.author.name
            author_name = "Shiba Bot"
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick
            author_name = ctx.message.author.nick
        else:
            tag_name = name
            author_name = ctx.message.author.nick
        
        await ctx.send(f"**{author_name}** đã gửi tình yêu siêu bự đến **{tag_name}** đóooooo <:meow_xoadau:759037054431658036>")

        author = ImageDraw.Draw(txt)
        author.text((170, 45), author_name, font=fnt, fill=(0, 0, 0, 255), anchor = "mm")
        
        tag = ImageDraw.Draw(txt)
        tag.text((210, 195), tag_name, font=fnt2, fill=(0, 0, 0, 255), stroke_width=2, stroke_fill=(255, 255, 255, 255), anchor = "mm")

        out = Image.alpha_composite(base, txt)
        out.save('luv.png')
        
        await ctx.send(file=discord.File('luv.png'))

    @commands.command(pass_context=True)
    async def shiba(self, ctx):
        # await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url='https://i.redd.it/y0o3u4ddkfs71.gif')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def corgi(self, ctx):
        # await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url='https://c.tenor.com/QfBQk0quoS8AAAAM/corgi-cute.gif')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def gudbot(self, ctx):
        await ctx.send(f"Cảm ơn nheee {ctx.author.name} <:meow_lovelybutt:759037054507810838>")
        embed = discord.Embed()
        embed.set_image(url='https://i.redd.it/isvpnmalxks71.gif')
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    async def kkk(self, ctx):
        img_list = [PATH + 'meme_img/kkk.jpg', PATH + 'meme_img/kkk2.jpg', PATH + 'meme_img/kkk3.jpg']

        laugh = "ka"
        cou = random.randint(3, 10)
        msg = ""
        if cou <= 5:
            choice = 0
        elif cou > 5 and cou <=8:
            choice = 1
        else:
            choice = 2

        for i in range(0, cou):
            msg += laugh

        await ctx.send(f"*{msg}*")
        await ctx.send(file=discord.File(img_list[choice]))