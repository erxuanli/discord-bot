import discord
from discord.ext import commands


class TrollFlori(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content.startswith("mh"):
            await message.channel.send("troll")
        if message.content.startswith("ms"):
            await message.channel.send("troll")
        if message.content.startswith("mwork"):
            await message.channel.send("troll")
        if message.content.startswith("mcd"):
            await message.channel.send("troll")
        if message.content.startswith("mdaily"):
            await message.channel.send("troll")
        if message.content.startswith("mvote"):
            await message.channel.send("troll")
        if message.content.startswith("mbj"):
            await message.channel.send("troll")
