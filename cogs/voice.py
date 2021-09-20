import disnake
from disnake import channel
from disnake.ext import commands
import asyncio
import random
from disnake.ext.commands.cooldowns import BucketType

from disnake.ext.commands.core import command, cooldown

class SunsetMusic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.voice_directory = r"/root/KaeyaTesingFInal/voicelines"
        self.ffmpeg_location = "/FFmpeg/bin"
        

    @commands.command(name="join")
    @cooldown(1,3, BucketType.user)
    async def joinchannel(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("Connected!")

    @commands.command(name="leave")
    @cooldown(1,3, BucketType.user)
    async def leavechannel(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected!")

def setup(bot):
    bot.add_cog(SunsetMusic(bot))