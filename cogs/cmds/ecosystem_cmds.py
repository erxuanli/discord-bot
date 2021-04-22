import discord
from discord.ext import commands

from discord.ext.commands import cooldown
from discord.ext.commands import BucketType

import os

from pymongo import MongoClient
from bson.objectid import ObjectId


class EcosystemCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.money = Money()

    @commands.command()
    @cooldown(1, 86400, BucketType.user)
    async def daily(self, ctx):
        try:
            self.money.change_money(str(ctx.author.id), 150)
        except KeyError:
            self.money.create_account(str(ctx.author.id), 150)
        await ctx.send("Collected daily money")

    @commands.command()
    async def wallet(self, ctx):
        await ctx.send(f"You have {self.money.get_money(str(ctx.author.id))} bot money")

    @commands.command()
    @commands.guild_only()
    async def transfer(self, ctx, member: discord.Member, amount: int):
        if member.id == ctx.author.id:
            await ctx.send("Cannot transfer money to yourself")
            return
        try:
            if amount <= self.money.get_money(str(ctx.author.id)):
                self.money.transfer_money(
                    str(ctx.author.id), str(member.id), amount)
                await ctx.send(f"Transfered {amount} to {member}")
            else:
                await ctx.send(f"Hmmm... i don't think you have that much money... You have {self.money.get_money(str(ctx.author.id))} bot money.")
        except ValueError:
            await ctx.send("Money value cannot be smaller than 1")
        except KeyError:
            await ctx.send(f"You or the person you want to transfer to does not have a account. Please collect your daily money with {self.client.command_prefix}daily. This will also create an account if you do not have one.")


class Money:
    def __init__(self):
        self.db_obj_id = "60819979ac2e4817c9eb6b29"
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
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {
                                        "$set": data}, upsert=True)

    def set_money(self, id: str, money: int):
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            data = money_collection.find_one(ObjectId(self.db_obj_id))
            if id not in data:
                raise KeyError
            else:
                data[id] = money
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {
                                        "$set": data}, upsert=True)

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
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {
                                        "$set": data}, upsert=True)

    def has_account(self, id: str) -> bool:
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            if id not in money_collection.find_one(ObjectId(self.db_obj_id)):
                return False
            return True

    def create_account(self, id: str, money: int = 0):
        data = {id: money}
        with self.client:
            db = self.client["ecosystem_cmds"]
            money_collection = db["money"]
            money_collection.update_one({"_id": ObjectId(self.db_obj_id)}, {
                                        "$set": data}, upsert=True)
