import discord
from discord.ext import commands
from config import TOKEN
from log import Logger

class SiriTest(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            help_command=None,
            activity=discord.Game("Siri (Confidential) | Not for commericial use")
        )  
        self.load_extension("cogs.main")
        self.logger = Logger.basicLogger(self)
        self.discordlog = Logger.discordLogger()
        

    async def on_message(self, message):
        if not message.author.bot: await self.process_commands(message)

    async def on_ready(self):
        self.logger.info("== This is bot is not for commericial use. ==")
        self.logger.info(f"Logged as {self.user.name}")

    async def on_command_error(self, context, exception):
        self.logger.error(f"An error occured while {context.command.name}. Traceback : {exception}")
    
    
bot = SiriTest()
bot.run(TOKEN, bot=True, reconnect=True)