import discord
from discord.ext import commands

from cogs.cmds.custom_checks import is_polarbear


class ManagementCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(is_polarbear)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send("Permission granted || Reason: PolarBear4u senpai")
        await member.add_roles(role)
        await ctx.send(f"added {role} to {member}")

    @commands.command()
    @commands.check(is_polarbear)
    async def remrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send("Permission granted || Reason: PolarBear4u senpai")
        await member.remove_roles(role)
        await ctx.send(f"{role} removed from {member}")
