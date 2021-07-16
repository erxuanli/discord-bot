import discord
from discord.ext import commands
from cogs.cmds.custom_checks import is_moderator, not_in_blacklist
from difflib import SequenceMatcher
import json
class ModeratorCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.collect_server_information()

    @commands.command()
    @commands.check(is_moderator)
    async def send(self, id, message):
        channel = self.client.get_channel(id)
        await channel.send(message)

    @commands.command()
    @commands.check(is_moderator)
    async def dm(self, ctx, message):
        await self.client.send_message(ctx.author, "hi")

    @commands.command()
    @commands.check(is_moderator)
    async def broadcast(self, ctx, *, message):
        for guild in self.client.guilds:
            for channel in guild.channels:
                if SequenceMatcher(None, channel.name,'general').ratio() > 0.6:
                    try:
                        await channel.send(message)
                    except:
                        pass

    @commands.command()
    @commands.check(is_moderator)
    async def listofservers(self, ctx):
        listofservers = [x for x in self.client.guilds]
        await ctx.send(listofservers)
    
    @commands.command()
    @commands.check(is_moderator)
    async def listofchannels(self, ctx, server):
        if isinstance(server, int):
            await ctx.send(self.listofservers[str(server)][1]["channels"])
        elif isinstance(server, str):
            for guild in self.listofservers:
                if self.listofservers[guild][0].lower() == server.lower():
                    await ctx.send(self.listofservers[str(guild)][1]["channels"]) 
        else:
            await ctx.send("Given server not found!")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modaddrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted")
        await member.add_roles(role)
        await ctx.send(f"added {role} to {member}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modremrole(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.send(f"Permission granted")
        await member.remove_roles(role)
        await ctx.send(f"{role} removed from {member}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modkick(self, ctx, member: discord.Member, *, reason: str = None):
        if member.id == ctx.author.id:
            await ctx.send(f"You can't kick yourself")
        else:
            await ctx.send(f"Permission granted")
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modban(self, ctx, member: discord.Member, *, reason: str = None):
        if member.id == ctx.author.id:
            await ctx.send(f"You can't ban yourself")
        else:
            await ctx.send(f"Permission granted")
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modunban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modnickname(self, ctx, member: discord.Member, *, nick: str):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname change: {member}'s nickname changed to {[nick]}")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modnicknames(self, ctx, *, n : str = None):
        nick = None
        for user in ctx.guild.members:
            if n is None:
                nick = user.name
            else:
                nick = n
            try:
                await user.edit(nick=nick)
                await ctx.send(f"changed {user}'s nickname to: [{nick}]")
            except discord.errors.Forbidden:
                await ctx.send(f"do not have enough permissions to change {user}'s nickname")
        await ctx.send("changed all nicknames that could be changed")

    @commands.command()
    @commands.guild_only()
    @commands.check(is_moderator)
    async def modclear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)

    def collect_server_information(self):
        self.listofservers = {}
        for guild in self.client.guilds:
            self.listofservers[str(guild.id)] = [guild.name, {"channels": [(x.id, x.name) for x in guild.channels]}]
