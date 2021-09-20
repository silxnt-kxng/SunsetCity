import disnake
from disnake.ext import commands
from disnake.ext.commands import when_mentioned_or
from disnake import guild

color = disnake.Colour.from_rgb(205, 148, 255)

PREFIX = "ss!"

intents = disnake.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=when_mentioned_or(PREFIX), case_insensitive=True, intents=intents)

@bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot running...")
    print("--------")
    membersall = []
    for guild in bot.guilds:
        for members in guild.members:
            membersall = guild.members
    
    intmemall = len(membersall)
	
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=(f"{intmemall} friends!")))

    print("Bot online!")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

extentions = ['cogs.fun', 'cogs.help', 'cogs.info', 'cogs.mis', 'cogs.start', 'cogs.voice']

if __name__ == '__main__':
    for x in extentions:
        bot.load_extension(x)

bot.run(TOKEN)
