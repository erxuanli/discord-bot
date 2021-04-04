import discord
from discord.ext import commands


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
        embed.add_field(name="**;help**",
                        value="That's this command xD", inline=False)
        embed.add_field(name="**;creator**",
                        value="creator of this useless bot", inline=False)
        embed.add_field(name="**;prefix**",
                        value="returns the current prefix", inline=False)
        embed.add_field(
            name="**;avatar [user]**", value="returns the avatar of the mentioned user", inline=False)
        embed.add_field(
            name="**;clear [int]**", value="clears channel [max 30]; do not spam", inline=False)
        embed.add_field(name="**;ping**", value="bot latency", inline=False)
        embed.add_field(name="**;time**",
                        value="returns the current time (of host location)", inline=False)
        embed.add_field(name="**;join**",
                        value="join vc", inline=False)
        embed.add_field(name="**;leave**",
                        value="leave vc", inline=False)
        embed.add_field(name="**;vcmute**",
                        value="mute all in vc", inline=False)
        embed.add_field(name="**;vcunmute**",
                        value="unmute all in vc", inline=False)
        embed.add_field(name="**;quote**",
                        value="returns random quote", inline=False)
        embed.add_field(name="**;ascii**",
                        value="converts to ascii / unicode", inline=False)
        embed.add_field(name="**;ranimegif**",
                        value="random anime gif", inline=False)
        embed.add_field(name="**;morse**",
                        value="converts to morse code", inline=False)
        embed.add_field(name="**;demorse**",
                        value="converts morse code back", inline=False)
        embed.add_field(name="**;sqfunc**",
                        value="returns zero points of a quadratic function", inline=False)
        embed.add_field(name="**;pi**", value="returns pi", inline=False)
        embed.add_field(name="**;dice [min] [max]**",
                        value="random number", inline=False)
        embed.add_field(name="**;sheeesh**",
                        value="completely useless cmd", inline=False)
        embed.add_field(name="**;melih**",
                        value="completely useless cmd", inline=False)
        embed.set_footer(
            text="Thanks for using this useless bot xD and greetings to all weebs xD")

        await ctx.send(embed=embed)

    @commands.command()
    async def creator(self, ctx):
        await ctx.send("PolarBear4u sennnnpaiiiiii")

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
