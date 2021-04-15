import discord
from discord.ext import commands, tasks

import os

import time

class OtherCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nicktimer_data = dict()
        self.refresh_nicktimers.start()

    @commands.command()
    @commands.guild_only()
    async def nicktimer(self, ctx, t : int = 5): # time in minutes
        if ctx.author.id in self.nicktimer_data:
            await ctx.send("Already started a timer")
        else:
            end_time = time.time() + (t * 60)
            self.nicktimer_data[ctx.author.id] = {"end_time": end_time, "ctx": ctx}
            await ctx.send(f"Timer set: {t} minutes")

    @tasks.loop(seconds=10)
    async def refresh_nicktimers(self):
        delete = []
        if self.nicktimer_data:
            for user in self.nicktimer_data:
                ctx = self.nicktimer_data[user]["ctx"]
                end_time = self.nicktimer_data[user]["end_time"]
                if time.time() >= end_time:
                    await ctx.author.edit(nick=ctx.author.name)
                    delete.append(user)
                else:
                    await ctx.author.edit(nick=f"Back in {int((end_time - time.time()) / 60)} min {round((end_time - time.time()) - (int((end_time - time.time()) / 60) * 60))} sec")
        for user in delete:
            del self.nicktimer_data[user]
        delete = []

    
