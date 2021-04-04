import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if "happy birthday" in message.content.lower():
            await message.channel.send("Happpppyyyyyy Birrrthhhhdayyyy!!!")
