import discord
from discord.ext import commands

client = commands.Bot(command_prefix=";")


@client.event
async def on_ready():
    print("Connected")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

client.run("ODI1NDIzMTkzNjk0Nzk3ODM0.YF9tQA.99TXXuF3hPpRgIPMdNMI-G63w4s")
