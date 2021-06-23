import discord
from discord.ext import commands

class VcActivityRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(before, after):
        if before.voice.voice_channel is None and after.voice.voice_channel is not None:
            try:
                print("join")
            except:
                print("join error")


    