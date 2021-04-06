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
    async def nicktimer(self, ctx, timer : int):
        self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["ctx"] = ctx
        self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["start"] = time.time()
        self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["end"] = self.nicktimer_info[str(ctx.guild.id)][str(ctx.author.id)]["start"] + timer

    @tasks.loop(seconds = 10)
    async def refresh_nicktimers(self):
        for server in self.nicktimer_info.keys():
            for user in self.nicktimer_info[server]:
                ctx = self.nicktimer_info[server][user]["ctx"]
                start = self.nicktimer_info[server][user]["start"]
                end = self.nicktimer_info[server][user]["end"]
                await ctx.author.edit(nick = str(end - start))




    