import discord
from discord.ext import commands
import json
import random

class LeagueOfLegends(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.listofplayers = []
        with open("./cogs/cmds/games/leagueoflegends/ultimate_names.json", "r") as file:
            self.ultimateNames = json.load(file)
    
    @commands.command()
    async def lolguess(self, ctx):
        if ctx.author.id not in self.listofplayers:
            point = 0
            while True:
                k = random.randint(0, len(self.ultimateNames))
                champ, ulti = self.ultimateNames[k]
                self.listofplayers.append([ctx.author.id, champ, ulti, point])
            
    @commands.Cog.listener()
    async def on_message(self, message):
        player = []
        for item in self.listofplayers:
            if message.author.id in item:
                player = item
                break
        if message == player[1]:
            player[3] += 1
            await message.channel.send(f"Good job! points: {player[3]}")
        elif message != player[1]:
            await message.channel.send(f"Game Over! The correct answer was {player[1]} | Total points: {player[3]}")
            self.listofplayers.pop(self.listofplayers.find(player))

    
    # def __init__(self, client):
    #     self.client = client
    #     with open("./cogs/cmds/games/leagueoflegends/ultimate_names.json", "r") as file:
    #         self.ultimateNames = json.load(file)
    #     self.waiting = False
    #     self.point = 0
        
    # @commands.command()
    # async def lolguess(self, ctx):
    #     self.waiting = True
    #     self.player = ctx.author.id
    #     while self.waiting:
    #         k = random.randint(0, len(self.ultimateNames)+1)
    #         self.champ, self.ulti = self.ultimateNames[k]
    #         await ctx.send(f"To what champion does {self.ulti} belong to")
        

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message == self.champ and self.waiting and self.player == message.author.id:
    #         self.point += 1
    #         await message.channel.send(f"good job! points: {self.point}")
    #     elif message != self.champ and self.waiting and self.player == message.author.id:
    #         self.waiting = False
    #         await message.channel.send(f"Game Over! The correct answer was {self.champ} | Total points: {self.point}")