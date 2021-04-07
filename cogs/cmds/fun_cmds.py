import discord
from discord.ext import commands

import json

import random
from sgp4.api import Satrec 
import julian
import datetime


class FunCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def satellite(self, ctx, quan : int = 1, *specific):
        if specific is None and quan != 0:
            count = 0
            with open("./cogs/cmds/cmd_utils/sgp4/active_satellites.json", "r") as file:
                satellites = json.load(file)
                for satellite in satellites:
                    if count >= quan:
                        return
                    s = satellites[satellite]["s"]
                    t = satellites[satellite]["t"] 
                    satellite_object = Satrec.twoline2rv(s, t)
                    jd, fr = julian.to_jd(datetime.datetime.now(), fmt = "jd"), 0.0
                    e, r, v = satellite_object.sgp4(jd, fr)
                    embed = discord.Embed(title = f"[{satellite}]", color = discord.Color.gold())
                    embed.add_field(name = "**True Equator Mean Equinox position (km)**", value = r, inline = False)
                    embed.add_field(name = "**True Equator Mean Equinox velocity (km/s)**", value = v, inline = False)
                    embed.set_footer(text = f"Julian Date [now]: [{jd}] || Fraction: [{fr}]")
                    await ctx.send(embed = embed)
                    count += 1
        elif specific is not None and quan == 0:
            with open("./cogs/cmds/cmd_utils/sgp4/active_satellites.json", "r") as file:
                satellites = json.load(file)
                for sat in specific:
                    if satellites.get(sat, None) is None:
                        await ctx.send(f"[{sat}] not found. Syntax Error or [{sat}] not in Database")
                        continue
                    else:
                        s = satellites[sat]["s"]
                        t = satellites[sat]["t"]
                        satellite_object = Satrec.twoline2rv(s, t)
                        jd, fr = julian.to_jd(datetime.datetime.now(), fmt = "jd"), 0.0
                        e, r, v = satellite_object.sgp4(jd, fr)
                        embed = discord.Embed(title = f"[{sat}]", color = discord.Color.gold())
                        embed.add_field(name = "**True Equator Mean Equinox position (km)**", value = r, inline = False)
                        embed.add_field(name = "**True Equator Mean Equinox velocity (km/s)**", value = v, inline = False)
                        embed.set_footer(text = f"Julian Date [now]: [{jd}] || Fraction: [{fr}]")
                        await ctx.send(embed = embed)
                        continue

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
