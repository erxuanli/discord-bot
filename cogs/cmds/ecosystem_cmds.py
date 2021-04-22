import discord
from discord.ext import commands

import os

from pymongo import MongoClient
from bson.objectid import ObjectId


class EcosystemCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.money = Money()

    @commands.command()
    async def daily(self, ctx):
        self.money.change_money(str(ctx.author.id), 150)

    @commands.command()
    async def transfer(self, ctx, member: discord.Member, amount: int):
        try:
            self.money.transfer_money(str(ctx.author.id), str(member.id), amount)
            await ctx.send(f"Transfered {amount} to {member}")
        except ValueError:
            await ctx.send("Money value cannot be smaller than 1")
        except KeyError:
            await ctx.send(f"You or the person you want to transfer to does not have a account. Please collect your daily money with {self.client.command_prefix}daily. This will also create an account if you do not have one.")

class Money:
    def __init__(self):
        self.db_obj_id = "60818ba0f0f26a6616b518bf"
        self.client = MongoClient(os.environ['MONGODB'])

    def change_money(self, id: str, money: int):
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            data = money_collection.find_one(ObjectId(self.db_obj_id))
            if id not in data:
                raise KeyError
            elif money <= 0:
                raise ValueError
            else:
                data[id] = data[id] + money
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {"$set": data}, upsert = True) 

    def set_money(self, id: str, money: int):
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            data = money_collection.find_one(ObjectId(self.db_obj_id))
            if id not in data:
                raise KeyError
            else:
                data[id] = money
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {"$set": data}, upsert = True) 

    def get_money(self, id: str) -> int:
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            data = money_collection.find_one(ObjectId(self.db_obj_id))
            if id not in data:
                raise KeyError
            else:
                return data[id]

    def transfer_money(self, id: str, to_id: str, money: int):
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            data = money_collection.find_one(ObjectId(self.db_obj_id))
            if id not in data or to_id not in data:
                raise KeyError
            elif money <= 0:
                raise ValueError
            else:
                data[id] = data[id] - money
                data[to_id] = data[to_id] + money
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {"$set": data}, upsert = True) 

    def has_account(self, id: str) -> bool:
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            if id not in money_collection.find_one(ObjectId(self.db_obj_id)):
                return False
            return True

    def create_account(self, id: str):
        data = {id: 0}
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {"$set": data}, upsert = True)

