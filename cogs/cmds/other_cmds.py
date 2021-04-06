import discord
from discord.ext import commands, tasks

import os

import time


class OtherCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nicktimer_info = dict()
        self.refresh_nicktimers.start()

    @commands.command()
    async def nicktimer(self, ctx, timer: int):
        start_time = time.time()
        self.nicktimer_info[str(ctx.author.id)] = {
            "ctx": ctx, "start": start_time, "end": start_time + timer}

    @tasks.loop(seconds=10)
    async def refresh_nicktimers(self):
        print("test loop")
        # for user in self.nicktimer_info.keys():
        #     ctx = self.nicktimer_info[user]["ctx"]
        #     start_time = self.nicktimer_info[user]["start"]
        #     end_time = self.nicktimer_info[user]["end"]
        #     await ctx.author.edit(nick = str(end_time - start_time))
