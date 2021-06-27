import discord
from discord.ext import commands

import json
import os

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

class VcActivityRoles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.udpate_stats_json()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            print(f"hi {member.name} / {member.id}")
            print(dir(member))
            print("\n\n")
            print(dir(before))
            print("\n\n")
            print(dir(after))
            print("\n\n")

    def udpate_stats_json(self):
        db_client = MongoClient(os.environ['MONGODB'])
        with db_client:
            db = db_client["activity"]
            prefix_collection = db["user_voice"]
            stats = prefix_collection.find_one(
                ObjectId("60d2fce20a8eed87da7c9f79"))
            with open("user_voice_stats.json", "w") as file:
                json.dump(json_util.dumps(stats), file)
            

    