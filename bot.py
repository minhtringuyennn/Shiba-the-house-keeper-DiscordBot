#!/usr/bin/python3
import configparser
import discord
from discord.ext import commands

# import youtube_dl
import pathlib
import string
import os
import default
import voice
import rand
import vote
import funny

# import music_bot
class MyBot(commands.Bot):
    def read_config(self):
        read_config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
        read_config.read(path)
        self.__TOKEN = read_config.get("config", "Token")
        self.PREFIX = read_config.get("config", "CommandPrefix")

    def __init__(self):
        intents = discord.Intents().all()
        self.read_config()
        super().__init__(command_prefix=self.PREFIX, intents=intents)
        super().remove_command('help')
    def run(self):
        super().run(self.__TOKEN ,reconnect=True)

if __name__ == "__main__":
    bot = MyBot()
    bot.add_cog(default.DefaultCommands(bot))
    bot.add_cog(rand.Random(bot))
    bot.add_cog(vote.Vote(bot))
    bot.add_cog(funny.Funny(bot))
    # bot.add_cog(music_bot.Music(bot))
    bot.run()
