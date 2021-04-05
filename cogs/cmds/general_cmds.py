import discord
from discord.ext import commands

import os

class GeneralCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="help",
                              description="all useless cmds are listed below",
                              color=discord.Color.purple())
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")
        embed.add_field(name=f"**{self.client.command_prefix}help**",
                        value="That's this command xD", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}creator**",
                        value="creator of this useless bot", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}prefix**",
                        value="returns the current prefix", inline=False)
        embed.add_field(
            name=f"**{self.client.command_prefix}avatar [user]**", value="returns the avatar of the mentioned user", inline=False)
        embed.add_field(
            name=f"**{self.client.command_prefix}clear [int]**", value="clears channel [max 30]; do not spam", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}ping**", value="bot latency", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}time**",
                        value="returns the current time (of host location)", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}join**",
                        value="join vc", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}leave**",
                        value="leave vc", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}vcmute**",
                        value="mute all in vc", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}vcunmute**",
                        value="unmute all in vc", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}quote**",
                        value="returns random quote", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}ascii**",
                        value="converts to ascii / unicode", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}ranimegif**",
                        value="random anime gif", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}morse**",
                        value="converts to morse code", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}demorse**",
                        value="converts morse code back", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}sqfunc**",
                        value="returns zero points of a quadratic function", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}pi**", value="returns pi", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}dice [min] [max]**",
                        value="random number", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}addrole [user] [role]**",
                        value="adds a role to an user", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}remrole [user] [role]**",
                        value="removes a role from an user", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}sheeesh**",
                        value="completely useless cmd", inline=False)
        embed.add_field(name=f"**{self.client.command_prefix}melih**",
                        value="completely useless cmd", inline=False)
        embed.set_footer(
            text="Thanks for using this useless bot xD and greetings to all weebs xD")

        await ctx.send(embed=embed)

    @commands.command()
    async def creator(self, ctx):
        await ctx.send(f"{os.environ['MY_DISCORD_TAG']} sennnnpaiiiiii")

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(self.client.command_prefix)

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(ctx.author.avatar_url)
        else:
            userAvatarUrl = user.avatar_url
            await ctx.send(userAvatarUrl)

    @commands.command()
    async def clear(self, ctx, amount=5):
        if amount > 30:
            await ctx.send("max amount 30")
        else:
            await ctx.channel.purge(limit=amount)
