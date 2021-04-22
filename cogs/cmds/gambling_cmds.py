import discord
from discord.ext import commands

class GamblingCmds(commands.Cog):
    def __init__(self, client):
        self.client = client