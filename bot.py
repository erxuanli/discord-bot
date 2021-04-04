from cogs.cmds.general_cmds import GeneralCmds
import discord
from discord.ext import commands

import random
import datetime
import math

# import keep_alive


client = commands.Bot(command_prefix=".", help_command=None)

client.add_cog(GeneralCmds(client))


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=";help || Stalking PolarBear4u#7025"))
    print(f"{client.user}: Connected")


# ---------------------- general commands -----------------------------------


# ---------------------- testing commands ----------------------------------



# ---------------------- vc commands -------------------------------------



# --------------------- fun commands --------------------------------------




# --------------------- math commands ----------------------------------------



# --------------------- dumb and troll commands -----------------------------


# ----------------------- non cmd responses ----------------------------------


@client.event
async def on_message(message):

    # ---------------------- happy responses ---------------------------------
    if "happy birthday" in message.content.lower():
        await message.channel.send("Happpppyyyyyy Birrrthhhhdayyyy!!!")

    # ---------------------- troll flori resposes ----------------------------
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

    await client.process_commands(message)


# keep_alive.keep_alive()
client.run("ODI3NTcyMDYyNTIzNjIxMzk2.YGc-iw.anV1EEUTLd_76gWlRysFA3YTk9c")
