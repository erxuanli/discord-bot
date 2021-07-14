import discord
from discord.ext import commands
import json
import random

class LeagueOfLegends(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("ultimate_names.json", "r") as file:
            self.ultimateNames = json.load(file)
        self.waiting = False
        self.point = 0
        
    @commands.command()
    async def lolguess(self, ctx):
        self.waiting = True
        self.player = ctx.author.id
        while self.waiting:
            k = random.randint(0, len(self.ultimateNames)+1)
            self.champ, self.ulti = self.ultimateNames[k]
            await ctx.send(f"To what champion does {self.ulti} belong to")
        

    @commands.Cog.listener()
    async def on_message(self, message):
        if message == self.champ and self.waiting and self.player == message.author.id:
            self.point += 1
            await message.channel.send(f"good job! points: {self.point}")
        elif self.waiting and self.player == message.author.id:
            self.waiting = False
            await message.channel.send(f"Game Over! The correct answer was {self.champ} | Total points: {self.point}")