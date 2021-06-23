import discord
from discord.ext import commands

class VcActivityRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print(dir(member))
        print("\n\n")
        print(dir(before))
        


    