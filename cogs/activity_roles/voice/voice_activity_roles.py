import discord
from discord.ext import commands, tasks

import json
import os

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

import time

class VcActivityRoles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.editing_json = False
        self.loaded = False
        self.database_id = "60d2fce20a8eed87da7c9f79"
        self.sync_stats_json()
        self.upload_json_to_database.start()
        

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

    @tasks.loop(seconds=5)
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
                    stats = json_stats
                stats_collection.update_one({"_id": ObjectId(self.database_id)}, {"$set": stats})
            


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
                json.dump(json_util.dumps(stats), file)
        self.loaded = True

            

    