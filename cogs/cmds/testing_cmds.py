import discord
from discord.ext import commands

import datetime


class TestingCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx, precision : int = 0):
        await ctx.send(f"Pong! {round(self.client.latency * 1000, precision)}ms")

    @commands.command()
    async def time(self, ctx):
        await ctx.send(datetime.datetime.now())
