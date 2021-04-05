import discord
from discord.ext import commands

import os

from datetime import datetime

from cogs.cmds.general_cmds import GeneralCmds
from cogs.cmds.testing_cmds import TestingCmds
from cogs.cmds.vc_cmds import VcCmds
from cogs.cmds.fun_cmds import FunCmds
from cogs.cmds.math_cmds import MathCmds
from cogs.cmds.dumb_cmds import DumbCmds
from cogs.cmds.management_cmds import ManagementCmds

from cogs.non_cmds.troll_flori import TrollFlori
from cogs.non_cmds.events import Events

from cogs.activity_roles.voice.voice_activity_roles import VcActivityRoles

client = commands.Bot(command_prefix=";", help_command=None)

client.add_cog(GeneralCmds(client))
client.add_cog(TestingCmds(client))
client.add_cog(VcCmds(client))
client.add_cog(FunCmds(client))
client.add_cog(MathCmds(client))
client.add_cog(DumbCmds(client))
client.add_cog(ManagementCmds(client))

client.add_cog(TrollFlori(client))
client.add_cog(Events(client))

client.add_cog(VcActivityRoles(client))


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=f";help || Stalking {os.environ['MY_DISCORD_TAG']}"))
    print(f"[{datetime.now()}] {client.user}: Connected")

client.run(os.environ['BOT_TOKEN'])

