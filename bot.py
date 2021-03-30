import discord
from discord.ext import commands

import random
import datetime
import math

client = commands.Bot(command_prefix=";", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=";help || Stalking PolarBear4u#7025"))
    print("Connected")


# ---------------------- general commands -----------------------------------
@client.command()
async def creator(ctx):
    await ctx.send("PolarBear4u sennnnpaiiiiii")


@client.command()
async def help(ctx):
    embed = discord.Embed(title="help",
                          description="all useless cmds are listed below",
                          color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")
    embed.add_field(name="**;help**",
                    value="That's this command xD", inline=False)
    embed.add_field(name="**;creator**", value="creator of this useless bot", inline=False)
    embed.add_field(name="**;prefix**", value="returns the current prefix", inline=False)
    embed.add_field(name="**;avatar [user]**", value="returns the avatar of the mentioned user", inline=False)
    embed.add_field(name="**;ping**", value="bot latency", inline=False)
    embed.add_field(name="**;time**", value="returns the current time", inline=False)
    embed.add_field(name="**;randomuser**", value="returns a random user", inline=False)
    embed.add_field(name="**;pi**", value="returns pi", inline=False)
    embed.add_field(name="**;dice [min] [max]**", value="random number", inline=False)
    embed.add_field(name="**;sheeesh**", value="completely useless cmd", inline=False)
    embed.add_field(name="**;melih**", value="completely useless cmd", inline=False)
    embed.set_footer(
        text="Thanks for using this useless bot xD and greetings to all weebs xD")

    await ctx.send(embed=embed)

@client.command()
async def prefix(ctx):
    await ctx.send(client.command_prefix) 


@client.command()
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(ctx.author.avatar_url)
    else:
        userAvatarUrl = user.avatar_url
        await ctx.send(userAvatarUrl)


# ---------------------- testing commands ----------------------------------
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def time(ctx):
    await ctx.send(datetime.datetime.now())

# --------------------- fun commands --------------------------------------
@client.command()
async def randomuser(ctx):
    await ctx.send(random.choice(ctx.guild.members))


# --------------------- math commands ----------------------------------------
@client.command()
async def pi(ctx):
    await ctx.send(math.pi)


@client.command()
async def dice(ctx, min, max):
    await ctx.send(random.randint(int(min), int(max)))


# --------------------- dumb and troll commands -----------------------------
@client.command()
async def sheeesh(ctx):
    await ctx.send("ruben cringemai 2.0?")


@client.command()
async def melih(ctx):
    await ctx.send("i'm gaaaaaayy xD")


client.run("ODI1NDIzMTkzNjk0Nzk3ODM0.YF9tQA.99TXXuF3hPpRgIPMdNMI-G63w4s")
