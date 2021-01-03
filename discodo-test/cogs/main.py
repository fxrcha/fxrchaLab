from re import A
import discord
from discord.ext import commands
from utils.embed import Embed
from log import Logger

class MainCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.logger = Logger.basicLogger(self)


    @commands.command(name="join")
    async def join(self, ctx):
        if not ctx.message.author.voice:
            embed = Embed.warn(title = "먼저 음성 채널에 들어와주세요!")
            return await ctx.send(embed=embed)
        await self.bot.Wonstein.connect(ctx.message.author.voice.channel)
        embed = Embed.default(
            title = f"성공적으로 {ctx.message.author.voice.channel}에 연결했습니다."
        )
        await ctx.send(embed=embed)
            

    @commands.command(name="play")
    async def play(self, ctx, *, query):
        Audio = self.bot.Wonstein.getVC(ctx.guild)
        if not Audio:
            embed = Embed.warn(title = "먼저 `!join`을 입력해주세요.")
            return await ctx.send(embed=embed)
        if not hasattr(Audio, "channel"):
            Audio.channel = ctx.message.channel
        Source = await Audio.loadSource(query)
        await ctx.send (f"{Source['data']['title']} 추가완료")


def setup(bot):
    bot.add_cog(MainCog(bot))