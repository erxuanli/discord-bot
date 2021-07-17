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

            

    