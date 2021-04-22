import discord
from discord.ext import commands

from cogs.cmds.ecosystem_cmds import Money

class GamblingCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.money = Money()