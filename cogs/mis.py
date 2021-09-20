from os import add_dll_directory, name
import disnake
from disnake.ext import commands
import random, time
from urllib.parse import quote_plus
import aiohttp
import json
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown
import requests
from .utils import formatting
from imports import color

class SunsetMisc(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(aliases=['calc'])
    async def calculate(self, ctx, *, q):
        await ctx.send(f"{q}={eval(q)}")

    @commands.command(aliases=['pick'])
    async def choose(self, ctx, *, choices: str):
        await ctx.send('I choose: {}'.format(random.choice(choices.split(" | "))))
    
    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("🏓 Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 Pong!  `{int(ping)}ms`")

    @commands.command()
    async def poll(self, ctx, *, title):
        embed = disnake.Embed(
            title=f"{ctx.message.author}'s poll!",
            description=f"{title}",
            color=color,
            timestamp=ctx.message.created_at
            )

        embed_message = await ctx.send(embed=embed)

        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")


    @commands.command(name="weather")
    @cooldown(1,3, BucketType.user)
    async def weather(self, ctx, *, city: str):
        api_key = "d56ded016a1a4e4339037079e9f4794f"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel
        
        if x["cod"] != "404":
            async with channel.typing():
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsius = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                embed = disnake.Embed(
                    title=f"Weather in {city_name}",
                    color=color,
                    timestamp=ctx.message.created_at
                    )
                embed.add_field(
                    name="Descripition", 
                    value=f"**{weather_description}**", 
                    inline=False
                )
                embed.add_field(
                name="Temperature(C)", 
                value=f"**{current_temperature_celsius}°C**", 
                inline=False
                )
                embed.add_field(
                    name="Temperature(F)",
                    value=f"**{current_temperature}**"
                )
                embed.add_field(
                    name="Humidity(%)", 
                    value=f"**{current_humidity}%**", 
                    inline=False
                )
                embed.add_field(
                    name="Atmospheric Pressure(hPa)", 
                    value=f"**{current_pressure}hPa**", 
                    inline=False
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/CMrsxdX/weather.png"
                )
                
                await channel.send(embed=embed)
        
        else:
            await channel.send("City not found.")

    @commands.command(name="covid")
    @cooldown(1,3, BucketType.user)
    async def covid(self, ctx, *, country: str):
        url = f"https://coronavirus-19-api.herokuapp.com/countries/{country}"
        stats = requests.get(url)
        json_stats = stats.json()
        country = json_stats["country"]
        totalCases = json_stats["cases"]
        todayCases = json_stats["todayCases"]
        totalDeaths = json_stats["deaths"]
        todayDeaths = json_stats["todayDeaths"]
        recovered = json_stats["recovered"]
        active = json_stats["active"]
        critical = json_stats["critical"]
        embed = disnake.Embed(
            title=f"**COVID-19 Status Of {country}**!", color=color, 
            timestamp=ctx.message.created_at
            )
        embed.add_field(
            name="**Total Cases**", 
            value=totalCases, 
            inline=True
            )
        embed.add_field(
            name="**Today Cases**", 
            value=todayCases, 
            inline=True
            )
        embed.add_field(
            name="**Total Deaths**", 
            value=totalDeaths, 
            inline=True
            )
        embed.add_field(
            name="**Today Deaths**", 
            value=todayDeaths, 
            inline=True
            )
        embed.add_field(
            name="**Recovered**", 
            value=recovered, 
            inline=True
        )
        embed.add_field(
            name="**Active**", 
            value=active, 
            inline=True
            )
        embed.add_field(
            name="**Critical**", 
            value=critical, 
            inline=True
            )
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SunsetMisc(bot))