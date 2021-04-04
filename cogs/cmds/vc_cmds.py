import discord
from discord.ext import commands


class VcCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def vcmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=True)

    @commands.command()
    async def vcunmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)
