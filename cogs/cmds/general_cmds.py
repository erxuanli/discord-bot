import discord
from discord.ext import commands

import os

from cogs.cmds.custom_checks import is_creator


class GeneralCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creator(self, ctx):
        await ctx.send(f"{os.environ['MY_DISCORD_TAG']} sennnnpaiiiiii")

    @commands.command()
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
    async def clear(self, ctx, amount=5):
        if amount > 30 and not is_creator(ctx):
            await ctx.send("max amount 30")
        else:
            await ctx.channel.purge(limit=amount)
