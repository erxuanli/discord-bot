import discord
from discord.ext import commands

import os
import datetime

from cogs.cmds.custom_checks import is_creator, is_moderator

from discord.ext.commands import cooldown
from discord.ext.commands import BucketType


class GeneralCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creator(self, ctx):
        await ctx.send(f"{os.environ['MY_DISCORD_TAG']} sennnnpaiiiiii")

    @commands.command()
    @commands.guild_only()
    async def prefix(self, ctx):
        await ctx.send(self.client.command_prefix)

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(ctx.author.avatar_url)
        else:
            userAvatarUrl = user.avatar_url
            await ctx.send(userAvatarUrl)

    @commands.command()
    @commands.guild_only()
    async def savatar(self, ctx):
        await ctx.send(ctx.guild.icon_url)

    @commands.command()
    @cooldown(1, 60, BucketType.user)
    @commands.guild_only()
    async def clear(self, ctx, amount=5):
        if amount > 30 and not is_moderator(ctx):
            await ctx.send("max amount 30")
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command()
    async def id(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send(f"ID [{ctx.guild.name}]: [{ctx.guild.id}] \nID [{ctx.author.name}]: [{ctx.author.id}]")
        else:
            await ctx.send(f"ID [{member.name}]: [{member.id}]")

    @commands.command()
    @commands.guild_only()
    async def info(self, ctx, member : discord.Member = None):
        user = member
        if user is None:
            user = ctx.author

        embed = discord.Embed(title = f"User Info [{str(user)} || {str(user.id)}]", color = discord.Color.red())

        fields = [("User Tag", str(user), True),
                  ("User ID", str(user.id), True),
                  ("Created at", user.created_at.strftime("%d.%m.%Y || %H:%M:%S"), True),
                  ("Joined at", user.joined_at.strftime("%d.%m.%Y || %H:%M:%S"), True),
                  ("Highest Role", user.top_role.mention, True),
                  ("Status", str(user.status), True)]

        for name, value, inline in fields:
            embed.add_field(name = name, value = value, inline = inline)

        embed.set_footer(text=f"Time (bot host location): {datetime.datetime.now()}")

        await ctx.send(embed = embed)
        
