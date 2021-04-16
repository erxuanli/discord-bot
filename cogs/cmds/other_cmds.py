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
        if str(ctx.author.id) in self.nicktimer_data:
            await ctx.send("Already started a timer")
        else:
            if not self.nicktimer_refreshing:
                if t <= 9_999_999_999_999:
                    end_time = time.time() + (t * 60)
                    self.nicktimer_data[str(ctx.author.id)] = {"end_time": end_time, "ctx": ctx}
                    await ctx.send(f"Timer set: {t} minutes")
                else:
                    await ctx.send("Timer must be shorter than 9,999,999,999,999 minutes")
            else:
                await ctx.send(f"Cannot start timer currently. All timers are refreshing. Please reuse the command.")

    @commands.command()
    @commands.guild_only()
    async def nicktimer_add(self, ctx, t : int = 1):
        if str(ctx.author.id) not in self.nicktimer_data:
            await ctx.send("You didn't set a timer")
        else:
            if not self.nicktimer_refreshing:
                if (int((self.nicktimer_data[str(ctx.author.id)]["end_time"] - time.time() / 60)) + t) <= 9_999_999_999_999:
                    self.nicktimer_data[str(ctx.author.id)]["end_time"] = self.nicktimer_data[str(ctx.author.id)]["end_time"] + (t * 60)
                    await ctx.send(f"Added {t} minutes to timer")
                else:
                    await ctx.send("Timer must be shorter than 9,999,999,999,999 minutes")
            else:
                await ctx.send(f"Cannot add timer currently. All timers are refreshing. Please reuse the command.")

    @commands.command()
    @commands.guild_only()
    async def nicktimer_stop(self, ctx):
        if str(ctx.author.id) not in self.nicktimer_data:
            await ctx.send("No timer running")
        else:
            if not self.nicktimer_refreshing:
                try:
                    del self.nicktimer_data[str(ctx.author.id)]
                    await ctx.author.edit(nick=ctx.author.name)
                    await ctx.send("Timer stopped")
                except discord.errors.Forbidden:
                    pass
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
                    try:
                        await ctx.author.edit(nick=ctx.author.name)
                        delete.append(user)
                    except discord.errors.Forbidden:
                        pass
                else:
                    try:
                        await ctx.author.edit(nick=f"Back in {int((end_time - time.time()) / 60)} min {round((end_time - time.time()) - (int((end_time - time.time()) / 60) * 60))} sec")
                    except discord.errors.Forbidden:
                        pass
        for user in delete:
            del self.nicktimer_data[user]
        delete = []
        self.nicktimer_refreshing = False

    

    
