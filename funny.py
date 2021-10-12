import discord
from discord.ext import commands
from random import randint
import random

class Funny(commands.Cog):
    #OwO what's this
    @commands.command()
    async def mock(self, ctx, *, input= ""): 
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
        await ctx.send("**OwO**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    @commands.command()
    async def OwO(self, ctx):
        await ctx.send("**OwO**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    #etou...
    @commands.command()
    async def etou(self, ctx, *, input = ""):
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
        if (ctx.message.author.id in [506827356489515020,340643391618547712,624210700528779266]):
            rate = randint(90, 100)
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