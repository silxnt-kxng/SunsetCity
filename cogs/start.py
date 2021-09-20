import disnake
from disnake import member, embeds, guild
from disnake import colour
from disnake.ext import commands
from disnake.ext.commands.core import command
from imports import color, url, image

class SunsetStart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="about", aliases=["info", "welcome"], brief="A short welcome to Sunset's interface")
    async def about(self, ctx):
        members = set()

        for guild in self.bot.guilds:
            for members in guild.members:
                membersall = guild.members
        
        membersall = len(membersall)

        introembed=disnake.Embed(
            title=f"Welcome `{ctx.message.author}`!",
            description="I am Sunset, a Discord bot designed to improve your experience here!. "
            f"I am currently on my Beta Version and my prefix is `ss!`. "
            f"I am serving all `{membersall}` members of Sunset City!. "
            "Before I go, say be sure to thank `silxnt_kxng#9439` for creating me and this server!",
            color=color,
            timestamp=ctx.message.created_at
        )
        introembed.set_thumbnail(
            url=url
        )
        introembed.set_image(
            url=image
        )
        await ctx.send(embed=introembed)

def setup(bot):
    bot.add_cog(SunsetStart(bot))