import discord
from discord.ext import commands, tasks

import os
from itertools import cycle

from datetime import datetime

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
from cogs.cmds.other_cmds import OtherCmds

from cogs.cmds.games.tictactoe.tictactoe import TictactoeCmds

from cogs.non_cmds.troll_flori import TrollFlori
from cogs.non_cmds.events import Events

from cogs.activity_roles.voice.voice_activity_roles import VcActivityRoles

from cogs.error_handling.error_handling_cmds import ErrorHandlerCmds

intents = discord.Intents.default()
intents.members = True
intents.presense = True

client = commands.Bot(command_prefix=";", help_command=None, intents=intents)

cogs_bool = True

cogs = [HelpCmds(client), GeneralCmds(client), TestingCmds(client), VcCmds(client), FunCmds(client), MathCmds(client), ScienceCmds(client), DumbCmds(
    client), ManagementCmds(client), ModeratorCmds(client), EcosystemCmds(client), OtherCmds(client), TictactoeCmds(client), TrollFlori(client), Events(client), VcActivityRoles(client), ErrorHandlerCmds(client)]

for cog in cogs:
    client.add_cog(cog)


bot_status = cycle([f";help || Stalking {os.environ['MY_DISCORD_TAG']}", "Collaboration with Frozen0wl#9220",
                   "Still in development UwU", f"bot host started at: {datetime.now()}"])


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


client.run(os.environ['BOT_TOKEN'])
