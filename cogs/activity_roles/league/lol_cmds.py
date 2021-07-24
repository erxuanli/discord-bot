import discord
from discord.ext import commands

import json
import os

import requests

import pymongo
from pymongo import MongoClient


class LolCmds(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.APIKey = "RGAPI-70112070-cf56-4ca7-bc6a-a87cb55c379d"
        self.regions = ["euw1", "br1", "eun1", "jp1", "kr", "la1", "la2", "na1", "oc1", "tr1", "ru"]
        self.ranks = {"IRON":"0", "BRONZE":"1", "SILVER":"2", "GOLD":"3", "PLATINUM":"4", "DIAMOND":"5", "MASTER":"6", "GRANDMASTER":"7", "CHALLENGER":"8"}

    @commands.command()
    async def test(self, ctx):
        hi = str(self.isverified(ctx.author.id))
        await ctx.send(hi)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def addlolrankrole(self, ctx,*, roles):
        roles = roles.split()
        cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["riotapi"]
        collection = db["roles"]

        roledic = {}
        for i in range(len(roles)):
            roledic[str(i)] = roles[i]

        post = {"_id":ctx.guild.id, "roles":roledic}
        if collection.find_one({"_id":ctx.guild.id}) is not None:
            collection.update_one({"_id":ctx.guild.id}, {"$set":{"roles":roledic}}, True)
            await ctx.send("Successfully updated roles")
        else:
            collection.insert_one(post)
            await ctx.send("")

    @commands.command()
    async def update(self, ctx):
        if not self.isverified(ctx.author.id):
            await ctx.send(f"You need to first verify your account. Use the command verify to do so")
            return
        cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["riotapi"]
        collection = db["verifiedlist"]

        result = collection.find_one({"id":ctx.author.id})
        id = result["_id"]
        region = result["region"]
        tier = self.getLeagueEntriesID(region, id, 0, "tier")
        num = self.ranks[tier]
        collection = db["roles"]
        result = collection.find_one({"_id":ctx.guild.id})
        serverrole = int(result["roles"][num][3:-1])
        role = ctx.guild.get_role(serverrole)
        await ctx.author.add_roles(role)
        permissions = []
        defaultpermissions = []
        for permission in ctx.guild.default_role.permissions:
            if permission[1] == True:
                defaultpermissions.append(permission[0])
        
        for permission in role.permissions:
            if permission[1] == True and permission[0] not in defaultpermissions:
                permissions.append(permission[0])
        
        permissions = str(permissions).replace("_", " ").replace("'", "")
        if len(permissions) > 0:
            await ctx.send(f"{role} role added. This role gives you the following permissions:\n{permissions[1:-1]}")
        else:
            await ctx.send(f"{role} role added. This role gives no extra permissions")
    @commands.command()
    async def verify(self, ctx, region, *, summonerName):
        if self.isverified(ctx.author.id):
            await ctx.send(f"This discord account is already connected with a lol account, you can use the changeverification or removeverification command to fix this issue")
            return
        if region + "1" in self.regions:
            region += "1"
        summonerName = summonerName.strip()
        try:
            code = self.verificationCode(region, summonerName)
        except:
            pass
        if str(ctx.author.id) == code:
            try:
                cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                db = cluster["riotapi"]
                collection = db["verifiedlist"]

                post = {"_id":self.getSummonerInfo(region, summonerName), "id":ctx.author.id, "region":region, "summonerName":summonerName, "accountId":self.getSummonerInfo(region, summonerName, "accountId")}
                collection.insert_one(post)
                await ctx.send("Successfully verified!")
            except:
                await ctx.send("This lol account is already connected with a discord id, you can use the changeverification command to change discord connection or removeverification to remove discord connection")
        else:
            await ctx.send(f"Please write your discord id: {ctx.author.id} to 'Verification' in the about section of your league of legends settings")
    

    @commands.command()
    async def changeverification(self, ctx, region, *, summonerName):
        if region +"1" in self.regions:
            region+="1"
        summonerName = summonerName.strip()
        try:
            code = self.verificationCode(region, summonerName)
        except:
            pass
        if str(ctx.author.id) == code:
            try:
                cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                db = cluster["riotapi"]
                collection = db["verifiedlist"]

                result = collection.find_one_and_update({"_id":self.getSummonerInfo(region, summonerName)}, {"id":ctx.author.id})
                await ctx.send("Verification has been changed")
            except:
                await ctx.send("This lol account is not verified")
        else:
            await ctx.send(f"Please write your discord id: {ctx.author.id} to 'Verification' in the about section of your league of legends settings")
    

    @commands.command()
    async def removeverification(self, ctx, region, *, summonerName):
        if region +"1" in self.regions:
            region+="1"
        summonerName = summonerName.strip()
        try:
            code = self.verificationCode(region, summonerName)
        except:
            pass
        if str(ctx.author.id) == code:
            try:
                cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                db = cluster["riotapi"]
                collection = db["verifiedlist"]

                collection.delete_one({"_id":self.getSummonerInfo(region, summonerName)})
                await ctx.send("Verification has been removed")
            except:
                await ctx.send("This lol account is already not verified")
        else:
            await ctx.send(f"Please write your discord id: {ctx.author.id} to 'Verification' in the about section of your league of legends settings")


    @commands.command()
    async def lolstats(self, ctx, region = "", *, summonerName = ""):
        if region + "1" in self.regions:
            region += "1"
        if region not in self.regions:
            cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db = cluster["riotapi"]
            collection = db["verifiedlist"]
            result = collection.find_one({"id":ctx.author.id})
            if result is not None:
                id = result["_id"]
                region = result["region"]
                stats = self.getLeagueEntriesID(region, id)
                stats = sorted(stats, key=lambda k: k['queueType']) 

                if len(stats) == 0:
                    await ctx.send(f"This summoner hasn't played any ranked games recently")
                else:
                    tier = stats[1]["tier"] 
                    rank = stats[1]["rank"]
                    summoner = stats[1]["summonerName"]
                    played = stats[1]["wins"] +stats[1]["losses"]
                    winrate = round(stats[1]["wins"] / played * 100)
                    lp = stats[1]["leaguePoints"]
                    wins = stats[1]["wins"]
                    losses = stats[1]["losses"]
                    await ctx.send(f"**{summoner}**\n{tier} {rank} [{lp}LP]\n{winrate}% winrate\nW{wins}; L{losses}")
        else:
            summonerName = summonerName.strip()
            stats = self.getLeagueEntries(region, summonerName)
            stats = sorted(stats, key=lambda k: k['queueType']) 
            tier = stats[1]["tier"] 
            rank = stats[1]["rank"]
            summoner = stats[1]["summonerName"]
            played = stats[1]["wins"] +stats[1]["losses"]
            winrate = round(stats[1]["wins"] / played * 100)
            lp = stats[1]["leaguePoints"]
            wins = stats[1]["wins"]
            losses = stats[1]["losses"]
            await ctx.send(f"**{summoner}**\n{tier} {rank} [{lp}LP]\n{winrate}% winrate\nW{wins}; L{losses}")

    @commands.command()
    async def lolflexstats(self, ctx, region = "", *, summonerName = ""):
        if region + "1" in self.regions:
            region += "1"
        isverified = self.isverified(ctx.author.id)
        if region not in self.regions and isverified:
            cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db = cluster["riotapi"]
            collection = db["verifiedlist"]
            result = collection.find_one({"id":ctx.author.id})
            if result is not None:
                id = result["_id"]
                region = result["region"]
                stats = self.getLeagueEntriesID(region, id)
                stats = sorted(stats, key=lambda k: k['queueType']) 

                if len(stats) == 0:
                    await ctx.send(f"This summoner hasn't played any ranked games recently")
                else:
                    tier = stats[0]["tier"] 
                    rank = stats[0]["rank"]
                    summoner = stats[0]["summonerName"]
                    played = stats[0]["wins"] +stats[0]["losses"]
                    winrate = round(stats[0]["wins"] / played * 100)
                    lp = stats[0]["leaguePoints"]
                    wins = stats[0]["wins"]
                    losses = stats[0]["losses"]
                    await ctx.send(f"**{summoner}**\n{tier} {rank} [{lp}LP]\n{winrate}% winrate\nW{wins}; L{losses}")
        else:
            summonerName = summonerName.strip()
            if not isverified:
                stats = self.getLeagueEntries(region, summonerName)
            else:
                cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                db = cluster["riotapi"]
                collection = db["verifiedlist"]
                result = collection.find_one({"id":ctx.author.id})
                id = result["_id"]
                stats = self.getLeagueEntriesID(id)
            stats = sorted(stats, key=lambda k: k['queueType']) 
            tier = stats[0]["tier"] 
            rank = stats[0]["rank"]
            summoner = stats[0]["summonerName"]
            played = stats[0]["wins"] +stats[0]["losses"]
            winrate = round(stats[0]["wins"] / played * 100)
            lp = stats[0]["leaguePoints"]
            wins = stats[0]["wins"]
            losses = stats[0]["losses"]
            await ctx.send(f"**{summoner}**\n{tier} {rank} [{lp}LP]\n{winrate}% winrate\nW{wins}; L{losses}")
        
    #---------------------   utils    ---------------------#

    def verificationCode(self, region, summonerName):
        if region + "1" in self.regions:
            region += "1"
        id = self.getSummonerInfo(region, summonerName)
        URL = f"https://{region}.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/{id}?api_key={self.APIKey}"
        response = requests.get(URL).json()
        return response

    def getSummonerInfo(self, region, summonerName, info = "id"):
        if region + "1" in self.regions:
            region += "1"
        URL = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={self.APIKey}"
        response = requests.get(URL).json()
        return response[info]

    def getLeagueEntries(self, region, summonerName, type = None, info = None):
        if region + "1" in self.regions:
            region += "1"
        id = self.getSummonerInfo(region, summonerName)
        
        URL = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={self.APIKey}"
        response = requests.get(URL).json()
        if info is None and type is None: 
            return response
        elif type is not None:
            if info is None:
                return response[type]
            else:
                return response[type][info]
    def getLeagueEntriesID(self, region, id, type = None, info = None):
        URL = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={self.APIKey}"
        response = requests.get(URL).json()
        if info is None and type is None: 
            return response
        elif type is not None:
            if info is None:
                return response[type]
            else:
                return response[type][info]

    def isverified(self, discordid):
        cluster = MongoClient("mongodb+srv://owl:ESIKO1juCf3bUkrk@frozen0wl.c6k33.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["riotapi"]
        collection = db["verifiedlist"]

        result = collection.find_one({"id":discordid})
        if result is not None:
            return True
        return False
    def matchhistory(self, region, accountId):
        URL = f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={self.APIKey}"
        response = requests.get(URL).json()
        return response # {"matches": [{"platformId": "EUW1","gameId": 5357124652,"champion": 1,"queue": 450,"season": 13,"timestamp": 1625696536337,"role": "DUO_SUPPORT","lane": "TOP"},{"platformId": "EUW1","gameId": 5118254679,"champion": 1,"queue": 420,"season": 13,"timestamp": 1614286643766,"role": "SOLO","lane": "MID"},{"platformId": "EUW1","gameId": 5054451993,"champion": 1, ...

    