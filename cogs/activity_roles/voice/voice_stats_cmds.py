import discord
from discord.ext import commands

from cogs.cmds.custom_checks import not_in_blacklist, is_moderator

import cogs.activity_roles.voice.utils as vcstatsutils

class VoiceStatsCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.check(not_in_blacklist)
    async def vcstats(self, ctx, member: discord.Member = None):
        user = member
        if user is None:
            user = ctx.author

        embed = discord.Embed(title = f"User VC Stats [{str(user)} || {str(user.id)}]", color = discord.Color.orange())

        vcat_hours, vcat_minutes, vcat_seconds = vcstatsutils.seconds_to_hours_minutes_seconds(vcstatsutils.user_all_time(str(ctx.guild.id), str(user.id)))
        vcatg_hours, vcatg_minutes, vcatg_seconds = vcstatsutils.seconds_to_hours_minutes_seconds(vcstatsutils.user_all_time_global(str(user.id)))
        vcat_hours_14, vcat_minutes_14, vcat_seconds_14 = vcstatsutils.seconds_to_hours_minutes_seconds(vcstatsutils.user(str(ctx.guild.id), str(user.id), 14))
        vcatg_hours_14, vcatg_minutes_14, vcatg_seconds_14 = vcstatsutils.seconds_to_hours_minutes_seconds(vcstatsutils.user_global(str(user.id), 14))

        fields = [(f"VC All Time [{ctx.guild}]", f"{vcat_hours} hour(s), {vcat_minutes} minute(s), {vcat_seconds} second(s)", False),
                  ("VC All Time [Global]", f"{vcatg_hours} hour(s), {vcatg_minutes} minute(s), {vcatg_seconds} second(s)", False),
                  (f"VC last 14 days [{ctx.guild}]", f"{vcat_hours_14} hour(s), {vcat_minutes_14} minute(s), {vcat_seconds_14} second(s)", False),
                  ("VC last 14 days [Global]", f"{vcatg_hours_14} hour(s), {vcatg_minutes_14} minute(s), {vcatg_seconds_14} second(s)", False),
                  (f"VC Joins All Time [{ctx.guild}]", str(vcstatsutils.user_all_time_joins(str(ctx.guild.id), str(user.id))), False),
                  (f"VC Leaves All Time [{ctx.guild}]", str(vcstatsutils.user_all_time_leaves(str(ctx.guild.id), str(user.id))), False),
                  (f"VC Joins last 14 days [{ctx.guild}]", str(vcstatsutils.user_joins(str(ctx.guild.id), str(user.id), 14)), False),
                  (f"VC Leaves last 14 days [{ctx.guild}]", str(vcstatsutils.user_leaves(str(ctx.guild.id), str(user.id), 14)), False),
                  ("VC Joins All Time [Global]", str(vcstatsutils.user_all_time_joins_global(str(user.id))), False),
                  ("VC Leaves All Time [Global]", str(vcstatsutils.user_all_time_leaves_global(str(user.id))), False),
                  ("VC Joins last 14 days [Global]", str(vcstatsutils.user_joins_global(str(user.id), 14)), False),
                  ("VC Leaves last 14 days [Global]", str(vcstatsutils.user_leaves_global(str(user.id), 14)), False)
                  ]

        for name, value, inline in fields:
            embed.add_field(name = name, value = value, inline = inline)

        embed.set_footer(text=f"saving stats when user leaves vc")

        await ctx.send(embed = embed)

    @commands.command()
    @commands.guild_only()
    @commands.check(not_in_blacklist)
    async def vctop(self, ctx, lookback_days: int = 0): 
        toplist = list()
        title = ""

        if lookback_days <= 0:
            toplist = vcstatsutils.user_all_time_top(str(ctx.guild.id), 10)
            title = f"VC User Top [{ctx.guild}]"
        else:
            toplist = vcstatsutils.user_top(str(ctx.guild.id), 10, lookback_days)
            title = f"VC User Top [{ctx.guild}] [Last {lookback_days} days]"    

        embed = discord.Embed(title = title, color = discord.Color.orange())    

        count = 1
        for ti, userid in toplist:
            user = await self.client.fetch_user(userid)
            hours, minutes, seconds = vcstatsutils.seconds_to_hours_minutes_seconds(ti)

            cap = f"[{count}] {user}"
            count += 1

            embed.add_field(name=cap, value=f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)", inline=False)

        embed.set_footer(text=f"saving stats when user leaves vc")

        await ctx.send(embed = embed)


    @commands.command()
    @commands.check(not_in_blacklist)
    async def vctopglobal(self, ctx, lookback_days: int = 0): 
        toplist = list()
        title = ""

        if lookback_days <= 0:
            toplist = vcstatsutils.user_all_time_global_top(10)
            title = f"VC User Top [Global]"
        else:
            toplist = vcstatsutils.user_global_top(10, lookback_days)
            title = f"VC User Top [Global] [Last {lookback_days} days]"  

        embed = discord.Embed(title = title, color = discord.Color.orange())

        count = 1
        for ti, userid in toplist:
            user = await self.client.fetch_user(userid)
            hours, minutes, seconds = vcstatsutils.seconds_to_hours_minutes_seconds(ti)

            cap = f"[{count}] {user}"
            count += 1

            embed.add_field(name=cap, value=f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)", inline=False)

        embed.set_footer(text=f"saving stats when user leaves vc")

        await ctx.send(embed = embed)

    @commands.command()
    @commands.check(not_in_blacklist)
    async def vctopserver(self, ctx, lookback_days: int = 0): 
        toplist = list()
        title = ""

        if lookback_days <= 0:
            toplist = vcstatsutils.server_all_time_top(10)
            title = f"VC Server Top"
        else:
            toplist = vcstatsutils.server_top(10, lookback_days)
            title = f"VC Server Top [Last {lookback_days} days]" 

        embed = discord.Embed(title = title, color = discord.Color.orange()) 

        count = 1
        for ti, serverid in toplist:
            server = self.client.get_guild(int(serverid))
            hours, minutes, seconds = vcstatsutils.seconds_to_hours_minutes_seconds(ti)

            cap = f"[{count}] {server}"
            count += 1

            embed.add_field(name=cap, value=f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)", inline=False)

        embed.set_footer(text=f"saving stats when user leaves vc")

        await ctx.send(embed = embed)

    @commands.command()
    @commands.check(not_in_blacklist)
    @commands.check(is_moderator)
    async def vcsj(self, ctx): # vc stats as a json file
        with open("user_voice_stats.json", "r") as file:
            await ctx.send("VC Stats JSON:", file=discord.File(file, "user_voice_stats.json"))
