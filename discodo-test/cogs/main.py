from logging import Logger
import discord
from discord.ext import commands
from log import Logger

class MainCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Logger.basicLogger(self)




def setup(bot):
    bot.add_cog(MainCog(bot))