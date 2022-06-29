import discord
from discord.ext import commands
import re
import emoji

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #inter_total = []

    @commands.command()
    async def createvote(self, ctx, *, id = ""):
        await ctx.message.delete()
        #print(ctx)
        if (id == ""):
            logs =  await ctx.channel.history(limit=1).flatten()
            msg = logs[0]
        else:
            msg = await ctx.channel.fetch_message(id)
        #print(msg.content)
        list = msg.content.split("\n")
        for lt in list:
            lookup = ""
            server_match = re.search(r'<a?:(\w+):(\d+)>', lt)
            custom_match = re.search(r':(\w+):', lt)
            if server_match:
                lookup = server_match.group(1)
                #print(lookup)
                await msg.add_reaction(discord.utils.get(ctx.message.guild.emojis, name=lookup))
            elif custom_match:
                lookup = custom_match.group(1)  
                #print(lookup)
                await msg.add_reaction(discord.utils.get(ctx.message.guild.emojis, name=lookup))
            else:
                for emj in lt.split(' '):
                    if emoji.is_emoji(emj):
                        await msg.add_reaction(emj)
        #try:
        #    await msg.remove_reaction("<:amongus_VOTED:764909622754017322>",self.bot.user)
        #except:
        #    pass
