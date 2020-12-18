#!/usr/bin/python3
import configparser
import discord
from discord.ext import commands
# import youtube_dl
import string
import os
import default
import voice
import rand
import vote
import funny
class MyBot(commands.Bot):
    def read_config(self):
        read_config = configparser.ConfigParser()
        read_config.read("./config/config.ini")
        self.__TOKEN = read_config.get("config", "Token")
        self.PREFIX = read_config.get("config", "CommandPrefix")
    def __init__(self):
        intents = discord.Intents().all()
        self.read_config()
        super().__init__(command_prefix=self.PREFIX, intents=intents)
        super().remove_command('help')
    def run(self):
        super().run(self.__TOKEN,reconnect=True)

if __name__ == "__main__":
    bot = MyBot()
    bot.add_cog(default.DefaultCommands(bot))
    bot.add_cog(rand.Random(bot))
    bot.add_cog(vote.Vote(bot))
    bot.add_cog(funny.Funny(bot))
    bot.run()

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


# Mocking Text Generator

