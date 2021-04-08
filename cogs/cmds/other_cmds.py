import discord
from discord.ext import commands, tasks

import os

import time


class OtherCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

