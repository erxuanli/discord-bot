import discord
from discord.ext import commands

import datetime

from cogs.cmds.custom_checks import not_in_blacklist

class TestingCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(not_in_blacklist)
    async def ping(self, ctx, precision : int = 0):
        await ctx.send(f"Pong! {round(self.client.latency * 1000, precision)}ms")

    @commands.command()
    @commands.check(not_in_blacklist)
    async def time(self, ctx):
        await ctx.send(datetime.datetime.now())
