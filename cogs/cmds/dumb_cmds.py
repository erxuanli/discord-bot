import discord
from discord.ext import commands


class DumbCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sheeesh(self, ctx):
        await ctx.send("ruben cringemai 2.0?")

    @commands.command()
    async def melih(self, ctx):
        await ctx.send("i'm gaaaaaayy xD")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("i luvvvv anime xD")
