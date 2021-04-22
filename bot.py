import discord
from discord.ext import commands, tasks

from pymongo import MongoClient
from bson.objectid import ObjectId

import os
from itertools import cycle

from datetime import datetime
import time

from cogs.cmds.custom_checks import is_moderator

from cogs.cmds.help_cmds import HelpCmds
from cogs.cmds.general_cmds import GeneralCmds
from cogs.cmds.testing_cmds import TestingCmds
from cogs.cmds.vc_cmds import VcCmds
from cogs.cmds.fun_cmds import FunCmds
from cogs.cmds.math_cmds import MathCmds
from cogs.cmds.science_cmds import ScienceCmds
from cogs.cmds.dumb_cmds import DumbCmds
from cogs.cmds.management_cmds import ManagementCmds
from cogs.cmds.moderator_cmds import ModeratorCmds
from cogs.cmds.ecosystem_cmds import EcosystemCmds
from cogs.cmds.gambling_cmds import GamblingCmds
from cogs.cmds.other_cmds import OtherCmds

from cogs.cmds.games.tictactoe.tictactoe import TictactoeCmds

from cogs.non_cmds.troll_flori import TrollFlori
from cogs.non_cmds.events import Events

from cogs.activity_roles.voice.voice_activity_roles import VcActivityRoles

from cogs.error_handling.error_handling_cmds import ErrorHandlerCmds

intents = discord.Intents.default()
intents.members = True
intents.presences = True

def get_prefix(client, message):
    db_client = MongoClient(os.environ['MONGODB'])
    with db_client:
        db = db_client["bot"]
        prefix_collection = db["prefix"]
        prefixes = prefix_collection.find_one(ObjectId("6081acc55efe1960648fb76b"))
        if str(message.guild.id) not in prefixes:
            prefixes[str(message.guild.id)] = ";"
            prefix_collection.update_one({"_id": ObjectId("6081acc55efe1960648fb76b")}, {"$set": prefixes}, upsert = True)
            return ";"
        else:
            return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, help_command=None, intents=intents)

cogs_bool = True

cogs = [HelpCmds(client), GeneralCmds(client), TestingCmds(client), VcCmds(client), FunCmds(client), MathCmds(client), ScienceCmds(client), DumbCmds(
    client), ManagementCmds(client), ModeratorCmds(client), EcosystemCmds(client), GamblingCmds(client), OtherCmds(client), TictactoeCmds(client), TrollFlori(client), Events(client), VcActivityRoles(client), ErrorHandlerCmds(client)]

for cog in cogs:
    client.add_cog(cog)


bot_status = cycle([f";help || Stalking {os.environ['MY_DISCORD_TAG']}", "Collaboration with Frozen0wl#9220",
                   "Still in development UwU", f"bot host started at: {time.ctime(time.time() + (2 * 60**2))}"])


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)
    change_status.start()
    print(f"[{datetime.now()}] {client.user}: Connected")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(name=next(bot_status)))


@client.command()
@commands.check(is_moderator)
async def debug(ctx):
    global cogs_bool
    if cogs_bool:
        for cog in cogs:
            client.remove_cog(cog.__class__.__name__)
        cogs_bool = not cogs_bool
        await ctx.send(f"debug: [{not cogs_bool}]")
    else:
        for cog in cogs:
            client.add_cog(cog)
        cogs_bool = not cogs_bool
        await ctx.send(f"debug: [{not cogs_bool}]")

@client.event
async def on_guild_join(guild):
    db_client = MongoClient(os.environ['MONGODB'])
    with db_client:
        db = db_client["bot"]
        prefix_collection = db["prefix"]
        prefixes = prefix_collection.find_one(ObjectId("6081acc55efe1960648fb76b"))
        prefixes[str(guild.id)] = ";"
        prefix_collection.update_one({"_id": ObjectId("6081acc55efe1960648fb76b")}, {"$set": prefixes}, upsert = True)

@client.event
async def on_guild_remove(guild):
    data = {str(guild.id): ""}
    db_client = MongoClient(os.environ['MONGODB'])
    with db_client:
        db = db_client["bot"]
        prefix_collection = db["prefix"]
        prefix_collection.update_one({"_id": ObjectId("6081acc55efe1960648fb76b")}, {"$unset": data})

@client.command()
@commands.guild_only()
async def prefix(ctx, prefix: str = None):
    p = None
    if prefix is None:
        p = ";"
    else:
        p = prefix
    db_client = MongoClient(os.environ['MONGODB'])
    with db_client:
        db = db_client["bot"]
        prefix_collection = db["prefix"]
        prefixes = prefix_collection.find_one(ObjectId("6081acc55efe1960648fb76b"))
        prefixes[str(ctx.guild.id)] = p.strip()
        prefix_collection.update_one({"_id": ObjectId("6081acc55efe1960648fb76b")}, {"$set": prefixes}, upsert = True)
    await ctx.send(f"Updated guild prefix to [{p}]")



client.run(os.environ['BOT_TOKEN'])
