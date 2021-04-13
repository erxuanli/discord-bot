import discord
from discord.ext import commands
from cogs.cmds.custom_checks import is_moderator


class ModeratorCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(is_moderator)
    async def broadcast(self, ctx, *, message):
        for guild in self.client.guilds:
            for channel in guild.channels:
                if(channel.name == 'general'):
                    await channel.send(message)
