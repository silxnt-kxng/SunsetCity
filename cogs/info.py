from time import time
import disnake
import aiohttp
from disnake.ext import commands
from disnake.ext.commands.cooldowns import BucketType
from disnake.ext.commands.core import cooldown
from imports import color, url

class SunsetInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="avatar")
    @cooldown(1,3, BucketType.user)
    async def avatar(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author
        
        embed = disnake.Embed(
            title=f"{user.name}\'s avatar",
            url=f"{user.display_avatar}",
            color=color,
            timestamp=ctx.message.created_at
        )
        embed.set_image(
        url=user.display_avatar
        )
        
        await ctx.send(embed=embed)
    
    @commands.command(name="userinfo")
    @cooldown(1,3, BucketType.user)
    async def userinfo(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author
        
        name = f'{user.name}'
        nick = f'{user.nick}'
        
        if nick is None:
            nick = name
        
        id = f'`{user.id}`'
        status = f'`{user.status}`' 
    
        if user.status is None:
            status = '`None`'
    
        voice_state = None if not user.voice else user.voice.channel
        voice = f'`{voice_state}`'
        activity = f'{user.activity}'
        toprole = f'{user.top_role.name}'
        if toprole == "@everyone":
            toprole = "None"
        
        roles = ' '.join([r.mention for r in user.roles][1:])
        avatar = f'{user.display_avatar}'
        embed = disnake.Embed(
            title=name + "'s Information", 
            color = color,
            timestamp=ctx.message.created_at
            )
        embed.set_thumbnail(
            url=avatar
            )
        embed.add_field(
            name="User Nickname",
            value=nick,
            inline=True
            )
        embed.add_field(
            name="User ID",
            value=id,
            inline=True
            )
        embed.add_field(
            name="Status",
            value=status,
            inline=True
            )
        embed.add_field(
            name="In Voice",
            value=voice,
            inline=False
            )
        embed.add_field(
            name="Custom Status",
            value=activity,
            inline=False
            )
        embed.add_field(
            name=f"Roles ({len(user.roles)-1})",
            value=roles,
            inline=False
            )
        embed.add_field(
            name="Highest Role",
            value=toprole,
            inline=False
            )
        embed.add_field(
            name='Account Created',
            value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
            inline=True
            )
        embed.add_field(
            name='Join Date',
        value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
        inline=True
        )
        
        await ctx.send(embed=embed)
    
    @commands.command(name="permissions", aliases=["iam"])
    @cooldown(1,3, BucketType.user)
    async def permissions(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author
        
        avatar = f'{user.display_avatar}'
        perms = '`,\n `'.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed = disnake.Embed(
            title=f'{user.name}' + "'s Permissions",
            description=f'`{perms}`',
            color = color,
            timestamp=ctx.message.created_at
            )
        embed.set_thumbnail(
            url=avatar
            )

        await ctx.send(embed=embed)

    @commands.command(name="servericon")
    @cooldown(1,3, BucketType.user)
    async def servericon(self, ctx):
        embed = disnake.Embed(
            title=f'{ctx.guild.name} server icon.',
            url=f"{ctx.guild.icon}",
            color=color,
            timestamp=ctx.message.created_at
            )
        embed.set_image(
            url=ctx.guild.icon
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name="serverinfo")
    @cooldown(1,3, BucketType.user)
    async def serverinfo(self, ctx):
        name = f'{ctx.guild.name}'
        owner = f'{ctx.guild.owner}'
        id = f'`{ctx.guild.id}`'
        icon = f'{ctx.guild.icon}'
        categories = f'{len(ctx.guild.categories)}'
        channels = f'{len(ctx.guild.channels)}'
        text_channels = f'{len(ctx.guild.text_channels)}'
        voice_channels = f'{len(ctx.guild.voice_channels)}'
        total_member = f'`{ctx.guild.member_count}`'
        online_members = f'{sum(member.status==disnake.Status.online and not member.bot for member in ctx.guild.members)}'
        offline_members = f'{sum(member.status==disnake.Status.offline and not member.bot for member in ctx.guild.members)}'
        humans = f'{sum(not member.bot for member in ctx.guild.members)}'
        bots = f'{sum(member.bot for member in ctx.guild.members)}'
        roles = f'`{len(ctx.guild.roles)}`'
        boost_level = f'{ctx.guild.premium_tier}'
        total_boosts = f'{ctx.guild.premium_subscription_count}'
        time = str(ctx.guild.created_at)
        time = time.split(" ")
        time = time[0]
        embed = disnake.Embed(
            title=name + " Server Information",
            color=color,
            timestamp=ctx.message.created_at
            )
        embed.set_thumbnail(
            url=icon
            )
        embed.add_field(
            name="Server Owner", value=owner, inline=True
            )
        embed.add_field(
            name="Server ID",
            value=id,
            inline=True
            )
        embed.add_field(
            name="‎",
            value="‎",
            inline=True
            )
        embed.add_field(
            name="Member Information:",
            value=f"All members: `{total_member}`\nHumans : `{humans}`\nBots: `{bots}`\nOnline members: `{online_members}`\nOffline members: `{offline_members}`",
            inline=True
        )
        embed.add_field(
            name="Server Informations:",
            value=f"Total roles: `{roles}`\nCategories: `{categories}`\nTotal channels: `{channels}`\nText channels: `{text_channels}`\nVoice channels: `{voice_channels}`\nBoost level: `{boost_level}`\nTotal boost: `{total_boosts}`\nServer created at: {time}",
            inline=True
        )

        await ctx.send(embed=embed)

    @commands.command(name="roleinfo", aliases=["role"])
    @cooldown(1,3, BucketType.user)
    async def roleinfo(self, ctx, *, role: disnake.Role):
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(role_created, since_created)
        members = ''
        i = 0
        
        for user in role.members:
            members += f'{user.name}, '
        
            i += 1
        
            if i > 30:
                break

        embed = disnake.Embed(
            colour=color,
            timestamp=ctx.message.created_at
            )
        embed.set_author(
            name=role.name
            )
        embed.add_field(
            name="Users", 
            value=len(role.members)
            )
        embed.add_field(
            name="Mentionable", 
            value=role.mentionable
            )
        embed.add_field(
            name="Hoist", 
            value=role.hoist
            )
        embed.add_field(
            name="Position", 
            value=role.position
            )
        embed.add_field(
            name="Managed", 
            value=role.managed
            )
        embed.add_field(
            name="Color", 
            value=role.colour
            )
        embed.add_field(
            name='Creation Date', 
            value=created_on
            )
        embed.add_field(
            name='Members', 
            value=members[:-2], 
            inline=False
            )
        embed.add_field(
            name=f'Role ID', 
            value=f'{role.id}', 
            inline=False
            )
        
        await ctx.send(embed=embed)

    @commands.command(name="channelinfo", aliases=["channel"])
    @cooldown(1,3, BucketType.user)
    async def channelinfo(self, ctx, channel: disnake.TextChannel = None):
        if channel is None:
            channel = ctx.message.channel

        embed = disnake.Embed(
            color=color, 
            description=channel.mention,
            timestamp=ctx.message.created_at
            )
        embed.add_field(
            name="Name", 
            value=channel.name
            )
        embed.add_field(
            name="Server", 
            value=channel.guild
            )
        embed.add_field(
            name="ID", 
            value=channel.id
            )
        embed.add_field(
            name="Category ID", 
            value=channel.category_id
            )
        embed.add_field(
            name="Position", 
            value=channel.position
            )
        embed.add_field(
            name="NSFW", 
            value=str(channel.is_nsfw())
            )
        embed.add_field(
            name="Members (cached)", 
            value=str(len(channel.members))
            )
        embed.add_field(
            name="Category", 
            value=channel.category
            )
        embed.add_field(
            name="Created", 
            value=channel.created_at.strftime("%d %b %Y %H:%M")
            )
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SunsetInfo(bot))