# bot.py
import os

import discord
from dotenv import load_dotenv

import random
import datetime
import time

from pi import pi

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
        # Setting `Playing ` status
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=";help || Stalking PolarBear4u#7025"))

    # # Setting `Streaming ` status
    # await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

    # # Setting `Listening ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

    # # Setting `Watching ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith(";hi"):
        await message.channel.send("I love anime")
    if message.content.startswith(";pi"):
        await message.channel.send(pi)
    if message.content.startswith(";me"):
        await message.channel.send(message.author)
    if message.content.startswith(";bot"):
        await message.channel.send(client.user)
    if message.content.startswith(";dice"):
        await message.channel.send(random.randint(1, 6))
    if message.content.startswith(";bigdice"):
        await message.channel.send(random.randint(1, 10000))
    if message.content.startswith(";message"):
        await message.channel.send(message.content)
    if message.content.startswith(";time"):
        await message.channel.send(datetime.datetime.now())
    if message.content.startswith(";creator"):
        await message.channel.send("PolarBear4u sennnnppaiiiiiiiiii")
    if message.content.startswith(";sheeesh"):
        await message.channel.send("ruben cringemai 2.0?")
    if message.content.startswith(";melih"):
        await message.channel.send("i'm gaaaayy xD")
    if message.content.startswith(";help"):
        await message.channel.send("**lit commands ehem...** \n\n;hi \n;pi \n;me \n;bot \n;dice \n;bigdice \n;message \n;time \n;creator \n;sheeesh \n;melih \n;randomuser \n;help")
    if message.content.startswith(";randomuser"):
        await message.channel.send(random.choice(message.channel.guild.members))
    if "happy birthday" in message.content.lower():
        await message.channel.send("Happpppyyyyyy Birrrthhhhdayyyy!!!")

    # troll flori
    if message.content.startswith("mh"):
        await message.channel.send("troll")
    if message.content.startswith("ms"):
        await message.channel.send("troll")
    if message.content.startswith("mwork"):
        await message.channel.send("troll")
    if message.content.startswith("mcd"):
        await message.channel.send("troll")
    if message.content.startswith("mdaily"):
        await message.channel.send("troll")
    if message.content.startswith("mvote"):
        await message.channel.send("troll")
    if message.content.startswith("mbj"):
        await message.channel.send("troll")
		        


client.run(TOKEN)