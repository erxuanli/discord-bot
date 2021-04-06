import discord
from discord.ext import commands

import os

from cogs.cmds.custom_checks import is_creator


class ManagementCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["arole"])
    @commands.check(is_creator)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted || Reason: {os.environ['MY_DISCORD_TAG']} senpai")
        await member.add_roles(role)
        await ctx.send(f"added {role} to {member}")

    @commands.command(aliases=["rrole"])
    @commands.check(is_creator)
    async def remrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted || Reason: {os.environ['MY_DISCORD_TAG']} senpai")
        await member.remove_roles(role)
        await ctx.send(f"{role} removed from {member}")

    @commands.command()
    @commands.check(is_creator)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        await ctx.send(f"Permission granted || Reason: {os.environ['MY_DISCORD_TAG']} senpai")
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}")

    @commands.command()
    @commands.check(is_creator)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        await ctx.send(f"Permission granted || Reason: {os.environ['MY_DISCORD_TAG']} senpai")
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}")

    @commands.command()
    async def nickname(self, ctx, member: discord.Member, nick : str):
        await member.edit(nick = nick)
        await ctx.send(f"Nickname change: {member}")
            
