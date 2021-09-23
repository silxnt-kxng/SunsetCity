from os import name, stat
import disnake
from disnake import activity
from disnake.enums import ActivityType
from disnake.ext import commands, tasks
from disnake.ext.commands import when_mentioned_or
from disnake import guild
import random
import asyncio
from imports import color

PREFIX = "ss!"

intents = disnake.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=when_mentioned_or(PREFIX), case_insensitive=True, intents=intents)

membersall = []
for guild in bot.guilds:
    for members in guild.members:
        membersall = guild.members

intmemall = len(membersall)

status = [

        "with Kxng's sanity!",
        "with Majin and Kiah!",
        "with Cassy and Kxng!",
        "Animal Crossing with Mobby!",
        "Deltarune with Mango!",
        "on SMPs with Keysmash!",
        "Pokemon with Lucky!",
        f"with {intmemall} members!",
        "with the Sunset City playlist!",
        "with Onler and Sin on the leaderboard!",
        "with Sunset City!",
        "with my brothers, Kaeya and Kokichi!",
        "ss!help"
        ]

@bot.remove_command("help")

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}. ID: {bot.user.id}")
	
@tasks.loop(seconds=15)
async def statuschange():
        await bot.wait_until_ready()

        statuschoice = random.choice(status)
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game(statuschoice))
        
statuschange.start()

extentions = ['cogs.fun', 'cogs.help', 'cogs.info', 'cogs.mis', 'cogs.start', 'cogs.voice']

if __name__ == '__main__':
	for x in extentions:
		bot.load_extension(x)


bot.run(TOKEN)
