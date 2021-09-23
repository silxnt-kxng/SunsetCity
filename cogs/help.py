from os import name
import random
from attr import validate
import disnake
from disnake import embeds
from disnake.ext import commands
import DiscordUtils
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown
from imports import url, color, image

description = "< > is required | [ ] is optional"

class HelpDialouge(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(name="help")
  @cooldown(1,3, BucketType.user)
  async def help(self, ctx):
    embedgeneral=disnake.Embed(
      title="Sunset Help Dialouge",
        color=color,
        timestamp=ctx.message.created_at
        )
    embedgeneral.add_field(
      name="Prefix",
      value="ss!"
    )
    embedgeneral.add_field(
      name="about",
      value="Intro command"
    )
    embedgeneral.add_field(
      name="Developer",
      value="**silxnt_kxng#9439**",
      inline=False
    )
    embedgeneral.set_thumbnail(
      url=url
      )
    embedgeneral.set_image(
      url=image
      )
#



#
    embedfun=disnake.Embed(
      title='Fun Commands',
      description=description,
      color=color,
      timestamp=ctx.message.created_at
    )
    embedfun.add_field(
        name="dice",
        value="Rolls a 6 sided die"
    )
    embedfun.add_field(
        name="flip / coin",
        value="Flip a coin and get heads or tails"
    )
    embedfun.add_field(
        name="question / 8ball / ask",
        value="Answers a question with a yes/no/maybe answer"
    )
    embedfun.add_field(
      name='dadjoke',
      value='Sunset tells a dad joke'
    )
    embedfun.add_field(
    name="playlist",
    value="Get the server Spotify playlist!"
    )
    embedfun.set_thumbnail(
      url=url
      )
    embedfun.set_image(
      url=image
    )
#



#
    embedinfo=disnake.Embed(
      title='Information', 
      description=description, 
      color=color,
      timestamp=ctx.message.created_at
      )
    embedinfo.add_field(
      name="userinfo [@user/userid]",
      value="Shows info about specified user (yourself if no member given)"
    )
    embedinfo.add_field(
      name="avatar [@user/userid]",
      value="Shows the specified user's avatar (yourself if no member given)"
    )
    embedinfo.add_field(
      name="serverinfo",
      value="Shows info about the server you're in"
    )
    embedinfo.add_field(
      name="servericon",
      value="Shows the server icon"
    )
    embedinfo.add_field(
      name="channelinfo (channel)",
      value="Shows info about the channel given (if no channel is give, then gived info about the current channel)"
    )
    embedinfo.add_field(
      name="permissions / iam",
      value="Shows your server permissions"
    )
    embedinfo.set_thumbnail(
      url=url
    )

    embedinfo.set_image(
      url=image
    )
#


#
    embedmisc=disnake.Embed(
      title='Miscellaneous Commands', 
      description=description,
      color=color,
      timestamp=ctx.message.created_at
      ) 
    embedmisc.add_field(
      name="help",
      value="Shows this menu"
    )
    embedmisc.add_field(
      name="weather <city>",
      value="Get the weather for the given city"
    )
    embedmisc.add_field(
      name="choose <option 1> | <option 2> | [option 3] | [...]",
      value="Chooses a random choice out of given options"
    )
    embedmisc.add_field(
      name="reminder <time> <reminder>",
      value="Reminds you of somethingby pinging you after the given time"
    )
    embedmisc.add_field(
      name="ping",
      value="Shows the bot's latency (how long it takes for info to get to Discord and back)"
    )
    embedmisc.add_field(
      name="covid <country>",
      value="Shows Covid-19 info by country"
    )
    embedmisc.add_field(
      name="poll <poll question>",
      value="Creates a poll"
    )
    embedmisc.add_field(
      name="calculate <mathematical expression>",
      value="Calculates the given math problem"
    )
    embedmisc.set_thumbnail(
      url=url
    )
    embedmisc.set_image(
      url=image
    )
#



#
    embedvoice=disnake.Embed(
      title='Voice Activity', 
      description=description,
      color=color,
      timestamp=ctx.message.created_at
      )
    embedvoice.add_field(
      name="join",
      value="Sunset will join the voice channel you're currently in"
    )
    embedvoice.add_field(
      name="leave",
      value="Remove Sunset from the current voice chat you're in"
    )
    embedvoice.add_field(
      name="play",
      value="Play a song from YouTube, SoundCloud, or Spotify"
    )
    embedvoice.add_field(
      name="pause",
      value="Pauses the player"
    )
    embedvoice.add_field(
      name="skip",
      value="Skips the current song"
    )
    embedvoice.add_field(
      name="nowplaying / np",
      value="Displayes the currently playing song"
    )
    embedvoice.add_field(
      name="queue / q",
      value="Displayes the queue"
    )
    embedvoice.add_field(
      name="loop",
      value="Loops the queue"
    )
    embedvoice.add_field(
      name="shuffle",
      value="Shuffles the queue"
    )
    embedvoice.set_image(
      url=image
    )
    embedvoice.set_thumbnail(
      url=url
    )
#


#   
    embedsupport=disnake.Embed(
      title='Support Kxng and his other bots!', 
      description="[**Click here**](https://www.patreon.com/silxnt_kxng) to go to the Patreon page!", 
      color=color,
      timestamp=ctx.message.created_at

      )
    embedsupport.set_thumbnail(
      url=url
    )
    embedsupport.set_image(
      url=image
    )
#


#
    embedmod=disnake.Embed(
      title="Moderation", 
      description=description, 
      color=color,
      timestamp=ctx.message.created_at
      )
    embedmod.add_field(
      name="warn <@user/userid>",
      value="Warns a user"
    )
    embedmod.add_field(
      name="kick <@user/userid>",
      value="Kicks a user"
    )
    embedmod.add_field(
      name="ban <@user/userid>",
      value="Bans a user"
    )
    embedmod.add_field(
      name="mute <@user/userid>",
      value="Mutes a user"
    )
    embedmod.add_field(
      name="unmute <@user/userid>",
      value="Unmutes a user that has been muted"
    )
    embedmod.add_field(
      name="nick <@user/userid> <new nickname>",
      value="Nicknames the user"
    )
    embedmod.add_field(
      name="k.purge <number of messages",
      value="Deletes a given number of messages"
    )
    embedmod.add_field(
      name="purge <number of messages> <@user/userid>",
      value="Purges a given number of messages by a given user"
    )
    embedmod.set_thumbnail(
      url=url
    )
    embedmod.set_image(
      url=image
    )

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
    paginator.add_reaction('⏪', "first")
    paginator.add_reaction('◀', "back")
    paginator.add_reaction('▶', "next")
    paginator.add_reaction('⏩', "last")
    embeds = [embedgeneral, embedfun, embedinfo, embedmisc, embedvoice, embedsupport, embedmod]
    await paginator.run(embeds)
#




#
  @commands.command(name="ownerhelp", aliases=['imhome', 'home', 'me'])
  async def ownerhelp(self, ctx):
    members = set()

    for guild in self.bot.guilds:
      for members in guild.members:
        membersall = guild.members

    membersall = len(membersall)
  
    embed=disnake.Embed(
        title=f"Welcome home, King.", 
        description="What I've been up to:",
        color=color,
        timestamp=ctx.message.created_at
        )
    embed.add_field(
        name="My default prefix:",
        value="ss!"
        )
    embed.add_field(
        name="Stats",
        value=f"Sunset City has {membersall} members! Well done!",
        inline=False 
      )
    embed.set_image(
        url=image
      )
        
    if ctx.author.id == 422835542653272066:
      await ctx.send(embed=embed)
    
    elif ctx.author.id != 422835542653272066:
      await ctx.send(random.choice("Nice try!", "Rip bozo", "You're not Kxng, silly!", "Better luck next time!"))

def setup(bot):
  bot.add_cog(HelpDialouge(bot))
