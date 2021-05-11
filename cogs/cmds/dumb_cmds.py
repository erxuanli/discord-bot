import discord
from discord.ext import commands

from cogs.cmds.custom_checks import not_in_blacklist
class DumbCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(not_in_blacklist)
    async def sheeesh(self, ctx):
        await ctx.send("ruben cringemai 2.0?")

    @commands.command()
    @commands.check(not_in_blacklist)
    async def melih(self, ctx):
        await ctx.send("i'm gaaaaaayy xD")

    @commands.command()
    @commands.check(not_in_blacklist)
    async def erxuan(self, ctx):
        await ctx.send("Senpai (っ °Д °;)っ")

    
