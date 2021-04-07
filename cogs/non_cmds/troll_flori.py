import discord
from discord.ext import commands

from cogs.cmds.custom_checks import is_flori

class TrollFlori(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.troll_flori_bool = True

    @commands.Cog.listener()
    async def on_message(self, message):
        if is_flori(message) and self.troll_flori_bool:
            await message.channel.send("troll")

    @commands.command()
    async def troll_flori(self, ctx):
        if not is_flori(ctx):
            self.troll_flori_bool = not self.troll_flori_bool
            await ctx.send(f"Troll Flori: [{self.troll_flori_bool}]")
        else:
            await ctx.send("Nononononononono (╯°□°）╯︵ ┻━┻")

