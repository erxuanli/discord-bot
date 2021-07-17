import discord
from discord.ext import commands, tasks

import json
import os

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

import time
import datetime

from cogs.cmds.custom_checks import not_in_blacklist, is_moderator

import cogs.activity_roles.voice.utils as vcstatsutils
class VcActivityRoles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.footer_message = "our website: https://chi-discord-bot.github.io/"
        self.editing_json = False
        self.loaded = False
        self.database_id = "60d2fce20a8eed87da7c9f79"
        self.sync_stats_json()
        self.upload_json_to_database.start()

    # vc roles commands and functions ---------------------------------------------
    @commands.command(aliases=["vcss", "vcssetup", "vcstatssetup", "voicechannelstatssetup"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    @commands.check(not_in_blacklist)
    async def voice_channel_stats_setup(self, ctx, category: str = None, role: discord.Role = None, needed_time: int = 0):   
        cmd_prefix = self.client.command_prefix(self.client, ctx)[2]     
        
        if category is None:
            embed = discord.Embed(title="vc activity roles [menu]",
                                    description="UwU",
                                    color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}vcss roles**", "use this command to add a role to activity roles", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)  

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        elif category == "roles":
            embed = discord.Embed(title="vc activity roles [roles menu]",
                                description="UwU",
                                color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}vcss addrole**", "use this command to add a role to activity roles", False),
                      (f"**{cmd_prefix}vcss remrole**", "use this command to add a role to activity roles", False),
                      (f"**{cmd_prefix}vcss showroles**", "use this command to add a role to activity roles", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)  

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        elif category == "addrole":
            pass

        elif category == "remrole":
            pass

        elif category == "showroles":
            pass


    # commands -----------------------------------------------------------------------
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


    # syncing and collecting vc stats -----------------------------------------------
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):    
        stats = None
        self.editing_json = True
        with open("user_voice_stats.json", "r") as file: # loading existing stats
            stats = json.loads(json.load(file))
        with open("user_voice_stats.json", "w") as file: # writing new stats
            if stats is None:
                stats = dict()
            if before.channel is None and after.channel is not None: # user joining vc
                stats = self.update_stats_json_join(stats.copy(), member)
            elif before.channel is not None and after.channel is None: # user leaving vc
                stats = self.update_stats_json_leave(stats.copy(), member)
            json.dump(json_util.dumps(stats), file)
        self.editing_json = False

    @tasks.loop(seconds=300) # every 5 minutes
    async def upload_json_to_database(self):
        if not self.loaded: 
            pass
        else:
            db_client = MongoClient(os.environ['MONGODB'])
            with db_client:
                db = db_client["activity"]
                stats_collection = db["user_voice"]
                stats = stats_collection.find_one(
                    ObjectId(self.database_id))
                with open("user_voice_stats.json", "r") as file:
                    json_stats = json.loads(json.load(file))
                    stats["data"] = json_stats
                stats_collection.update_one({"_id": ObjectId(self.database_id)}, {"$set": stats}, upsert=True)
        self.sync_stats_json()
            


    def update_stats_json_join(self, dic, member) -> dict:
        if str(member.guild.id) not in dic: # new server
            dic[str(member.guild.id)] = {str(member.id) : {"jlvc" : [[time.time()]]}}
            return dic
        elif str(member.id) not in dic[str(member.guild.id)]: # new member
            dic[str(member.guild.id)][str(member.id)] = {"jlvc" : [[time.time()]]}
        else:
            if len(dic[str(member.guild.id)][str(member.id)]["jlvc"][-1]) <= 1: # one or less time stamp
                dic[str(member.guild.id)][str(member.id)]["jlvc"][-1] = [time.time()]
            elif len(dic[str(member.guild.id)][str(member.id)]["jlvc"][-1]) == 2:
                dic[str(member.guild.id)][str(member.id)]["jlvc"].append([time.time()])
            else:
                dic[str(member.guild.id)][str(member.id)]["jlvc"].pop(-1)
                dic[str(member.guild.id)][str(member.id)]["jlvc"].append([time.time()])
        return dic


    def update_stats_json_leave(self, dic, member) -> dict:
        if str(member.guild.id) not in dic: # new server --> do nothing
            return dic 
        elif str(member.id) not in dic[str(member.guild.id)]: # new member --> do nothing
            return dic
        else:
            if len(dic[str(member.guild.id)][str(member.id)]["jlvc"][-1]) == 0:
                return dic
            elif len(dic[str(member.guild.id)][str(member.id)]["jlvc"][-1]) == 1:
                dic[str(member.guild.id)][str(member.id)]["jlvc"][-1].append(time.time())
            else:
                return dic
        return dic

                      

    def sync_stats_json(self): 
        db_client = MongoClient(os.environ['MONGODB'])
        with db_client:
            db = db_client["activity"]
            stats_collection = db["user_voice"]
            stats = stats_collection.find_one(
                ObjectId(self.database_id))
            with open("user_voice_stats.json", "w") as file:
                json.dump(json_util.dumps(stats["data"]), file)
        self.loaded = True

            

    