import discord
from discord.ext import commands, tasks

import os

import time

class OtherCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nicktimer_info = dict()
        self.test_nick_change.start()

    @commands.command()
    async def nicktimer(self, ctx, timer : int):
        self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["start"] = time.time()
        self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["timer"] = timer

    @tasks.loop(seconds = 10)
    async def refresh_nicktimers(self):
        pass

    @tasks.loop(seconds = 10)
    async def test_nick_change(self):
        user = self.client.get_user(172002275412279296)
        user.edit(nick = "test")



    