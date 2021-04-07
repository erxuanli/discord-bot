import discord
from discord.ext import commands

import json

from sgp4.api import Satrec 
import julian
import datetime

class ScienceCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def satellite(self, ctx, quan : int = 1):
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
                