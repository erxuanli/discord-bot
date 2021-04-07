import discord
from discord.ext import commands

import json

import random
from sgp4.api import Satrec 


class FunCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def satellite(self, ctx, quan : int):
        count = 0
        with open("./cogs/cmds/cmd_utils/sgp4/active_satellites.json", "r") as file:
            satellites = json.load(file)
            for satellite in satellites:
                if count >= quan:
                    return
                s = satellites[satellite]["s"]
                t = satellites[satellite]["t"] 
                satellite_object = Satrec.twoline2rv(s, t)
                jd, fr = 2458827, 0.362605
                e, r, v = satellite_object.sgp4(jd, fr)
                embed = discord.Embed(title = f"[{satellite}]", color = discord.Color.gold())
                embed.add_field(name = "**r**", value = r, inline = False)
                embed.add_field(name = "**v**", value = v, inline = False)
                embed.set_footer(text = f"jd: [{jd}] || fr: [{fr}]")
                await ctx.send(embed = embed)
                count += 1

    @commands.command()
    async def quote(self, ctx):
        with open("./cogs/cmds/cmd_utils/quotes.json", "r") as file:
            quotes = json.load(file)
            ind = random.randint(0, len(quotes) - 1)
            await ctx.send(quotes[ind])

    @commands.command()
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
    async def ranimegif(self, ctx):
        with open("./cogs/cmds/cmd_utils/anime_gifs.json", "r") as file:
            anime_gifs = json.load(file)
            await ctx.send(anime_gifs[random.randint(0, len(anime_gifs) - 1)])
