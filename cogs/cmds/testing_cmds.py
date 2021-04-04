import discord
from discord.ext import commands

import datetime

class TestingCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


    @commands.command()
    async def time(self, ctx):
        await ctx.send(datetime.datetime.now())