import discord
from discord.ext import commands
from cogs.cmds.custom_checks import is_moderator
import os

from pymongo import MongoClient
from bson.objectid import ObjectId

import json

import random

from cogs.cmds.custom_checks import not_in_blacklist

class FunCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
   
    @commands.command()
    async def right(self, ctx, member: discord.Member):
        k = random(0, 1)
        pos_vocabulary = [["Absolutely " + member],["Yes " + member + ". You are right!"], ["Dead-on!"], ["Precisely!"]]
        neg_vocabulary = [["No, Screw you!"], ["Ahahahahah, you stupid " + member +"?"], ["I’m trying my absolute hardest to see things from your perspective, but I just can’t get my head that far up my a*s"], ["Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt"], ["Everyone’s entitled to act stupid once in awhile, but you really abuse the privilege."] ]
        pos = random(0, len(pos_vocabulary) - 1)
        neg = random(0, len(neg_vocabulary) - 1)
        if is_moderator():
            await ctx.send(f"Yes {member}, you are always right!")
        elif k == 0:
            await ctx.send(pos_vocabulary[pos])
        else:
            await ctx.send(neg_vocabulary[neg])
            
    @commands.command()
    @commands.check(not_in_blacklist)
    async def quote(self, ctx):
        with open("./cogs/cmds/cmd_utils/quotes.json", "r") as file:
            quotes = json.load(file)
            ind = random.randint(0, len(quotes) - 1)
            await ctx.send(quotes[ind])

    @commands.command()
    @commands.check(not_in_blacklist)
    async def morse(self, ctx, *sentence):
        with open("./cogs/cmds/cmd_utils/morse_code_dict.json", "r") as file:
            MORSE_CODE_DICT = json.load(file)
            res = ""
            for word in sentence:
                for char in word:
                    res += MORSE_CODE_DICT[char.upper()]
                    res += " "

            await ctx.send(res)

    @commands.command()
    @commands.check(not_in_blacklist)
    async def demorse(self, ctx, *sentence):
        with open("./cogs/cmds/cmd_utils/morse_code_dict.json", "r") as file:
            MORSE_CODE_DICT = json.load(file)
            div = dict()
            for key, value in MORSE_CODE_DICT.items():
                div[value] = key

            res = ""
            for mchar in sentence:
                res += div[mchar].lower()

            await ctx.send(res)

    @commands.command()
    @commands.check(not_in_blacklist)
    async def ascii(self, ctx, *sentence):
        res = ""
        for word in sentence:
            for char in word:
                res += str(ord(char))
                res += "/"
            res = res[:-1]
            res += " | "
        res = res[:-3]
        await ctx.send(res)

    @commands.command()
    @commands.check(not_in_blacklist)
    async def ranimegif(self, ctx):
        with open("./cogs/cmds/cmd_utils/anime_gifs.json", "r") as file:
            anime_gifs = json.load(file)
            await ctx.send(anime_gifs[random.randint(0, len(anime_gifs) - 1)])

    @commands.command()
    @commands.check(not_in_blacklist)
    async def note(self, ctx, *, n : str = None):
        obj_id = "607f305065c78e14e94bf714"
        data = dict()
        client = MongoClient(os.environ['MONGODB'])
        with client:
            db = client["fun_cmds"]
            notes_collection = db["note"]
            if notes_collection.find_one(ObjectId(obj_id)) is not None:
                data = notes_collection.find_one(ObjectId(obj_id))

            if n is None:
                data[str(ctx.author.id)] = "UwU"
            else:
                data[str(ctx.author.id)] = n
                
            notes_collection.update_one({"_id":ObjectId(obj_id)}, {"$set": data}, upsert = True)

            await ctx.send("saved changes")

    @commands.command()
    @commands.check(not_in_blacklist)
    async def rnote(self, ctx):
        obj_id = "607f305065c78e14e94bf714"
        data = dict()
        client = MongoClient(os.environ['MONGODB'])
        with client:
            db = client["fun_cmds"]
            notes_collection = db["note"]
            if notes_collection.find_one(ObjectId(obj_id)) is not None:
                data = notes_collection.find_one(ObjectId(obj_id))

            if str(ctx.author.id) not in data:
                await ctx.send(f"do not have a note. please create a note with {self.client.command_prefix(self.client, ctx)[2]}note")
            else:
                await ctx.send(data[str(ctx.author.id)])

