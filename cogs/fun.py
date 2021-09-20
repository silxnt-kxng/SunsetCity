import disnake
from disnake.ext import commands
import random, asyncio, aiohttp
from disnake.ext.commands import cooldown, BucketType
from disnake import embeds
from disnake import player, File
from imports import *

class SunsetFun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ask", aliases=["question", "8ball"], brief="Get a random 8-ball answer")
    @cooldown(1, 3, BucketType.user)
    async def ask(self, ctx):
        ques = disnake.Embed(
            title=f"Answering `{ctx.message.author}`'s question",
            description=f"{question()}",
            color=color,
            timestamp=ctx.message.created_at
        )
        ques.set_thumbnail(
            url=ctx.author.display_avatar
        )

        await ctx.send(embed=ques)
    
    @commands.command(name="dice")
    @cooldown(1,3, BucketType.user)
    async def dice(self, ctx):
        dice6=["1","2","3","4","5","6"]
        embed = disnake.Embed(
            title=f"Rolled a dice! 🎲",
            description=f"It landed on {random.choice(dice6)}!",
            colour=color,
            timestamp=ctx.message.created_at)
        
        await ctx.send(embed=embed)
    
    @commands.command(name="coin", aliases=['flip'])
    @cooldown(1,3, BucketType.user)
    async def coin(self, ctx):

        coinresult = ["heads! Was this the result you wanted?", "tails! Was this the result you wanted?", "on its side! How did that happen?"]

        embed = disnake.Embed(
            title=f"Flipped a coin for `{ctx.message.author}`",
            description=f"It landed on {random.choice(coinresult)}",
            colour=color,
            timestamp=ctx.message.created_at
            )

        await ctx.send(embed=embed)

    @commands.command(name="dadjoke")
    @cooldown(1,3, BucketType.user)
    async def dadjoke(self, ctx):
        api = "https://icanhazdadjoke.com/"
        async with aiohttp.request("GET", api, headers={"Accept": "text/plain"}) as r:
            result = await r.text(encoding="UTF-8")
        
        await ctx.send(f"`{result}`")

def setup(bot):
    bot.add_cog(SunsetFun(bot))