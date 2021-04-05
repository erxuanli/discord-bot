import discord
from discord.ext import commands

import math
import random


class MathCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.pi_num = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951"

    @commands.command()
    async def sqfunc(self, ctx, a: float, b: float, c: float):
        x1, x2 = None, None
        b = b / a
        c = c / a
        v = -(b / 2)
        try:
            d = math.sqrt((b / 2)**2 - c)
            if d == 0.0:
                await ctx.send(v)
            elif d > 0:
                x1 = v + d
                x2 = v - d
                await ctx.send(f"{x1} {x2}")
        except ValueError:
            await ctx.send("There aren't any zero points")

    @commands.command()
    async def pi(self, ctx):
        await ctx.send(self.pi_num)

    @commands.command()
    async def dice(self, ctx, min, max):
        await ctx.send(random.randint(int(min), int(max)))
