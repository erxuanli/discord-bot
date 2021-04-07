import discord
from discord.ext import commands

from cogs.cmds.custom_checks import is_flori

class TrollFlori(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if is_flori(message):
            await message.channel.send("troll")

