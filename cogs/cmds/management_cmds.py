import discord
from discord.ext import commands

class ManagementCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["arole"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted")
        await member.add_roles(role)
        await ctx.send(f"added {role} to {member}")

    @commands.command(aliases=["rrole"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def remrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted")
        await member.remove_roles(role)
        await ctx.send(f"{role} removed from {member}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        await ctx.send(f"Permission granted")
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        await ctx.send(f"Permission granted")
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def unban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user}")

    @commands.command()
    @commands.guild_only()
    async def nickname(self, ctx, member: discord.Member, nick: str):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname change: {member}")
