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
import music_bot
import database

class MyBot(commands.Bot):
    def read_config(self):
        read_config = configparser.ConfigParser()
        read_config.read("./config/config.ini")
        self.__TOKEN = read_config.get("default", "Token")
        self.PREFIX = read_config.get("default", "Prefix")
    def __init__(self):
        self.read_config()
        try:
            self.db = database.DB()
        except:
            pass
        intents = discord.Intents().all()
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
    bot.add_cog(music_bot.Music(bot))
    bot.run()

