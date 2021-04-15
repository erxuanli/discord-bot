import discord
from discord.ext import commands, tasks

import os

import time

class OtherCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nicktimer_data = dict()
        self.nicktimer_refreshing = False
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

    @commands.command()
    @commands.guild_only()
    async def nicktimer_add(self, ctx, t : int = 1):
        if ctx.author.id not in self.nicktimer_data:
            await ctx.send("You didn't set a timer")
        else:
            if not self.nicktimer_refreshing:
                self.nicktimer_data[ctx.author.id] = self.nicktimer_data[ctx.author.id]["end_time"] + (t * 60)
                await ctx.send(f"Added {t} minutes to timer")
            else:
                await ctx.send(f"Cannot add timer currently. All timers are refreshing. Please reuse the command.")

    @commands.command()
    @commands.guild_only()
    async def nicktimer_stop(self, ctx):
        if ctx.author.id not in self.nicktimer_data:
            await ctx.send("No timer running")
        else:
            if not self.nicktimer_refreshing:
                del self.nicktimer_data[ctx.author.id]
                await ctx.author.edit(nick=ctx.author.name)
                await ctx.send("Timer stopped")
            else:
                await ctx.send(f"Cannot stop timer currently. All timers are refreshing. Please reuse the command.")

    @tasks.loop(seconds=5)
    async def refresh_nicktimers(self):
        self.nicktimer_refreshing = True
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
        self.nicktimer_refreshing = False

    

    
