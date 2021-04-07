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
        with open("./utils/sgp4/active_satellites.json", "r") as file:
            satellites = json.load(file)
            for satellite in satellites:
                if count >= quan:
                    return
                s = satellites[satellite]["s"]
                t = satellites[satellite]["t"] 
                satellite_object = Satrec.twoline2rv(s, t)
                jd, fr = 2458827, 0.362605
                e, r, v = satellite_object.sgp4(jd, fr)
                await ctx.send(r)
                await ctx.send(v)
                count += 1

    @commands.command()
    async def quote(self, ctx):
        quotes = ["“Be yourself; everyone else is already taken.” ― Oscar Wilde",
                  "“I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.” ― Marilyn Monroe",
                  "“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.” ― Albert Einstein",
                  "“So many books, so little time.” ― Frank Zappa",
                  "“A room without books is like a body without a soul.” ― Marcus Tullius Cicero"]
        ind = random.randint(0, len(quotes) - 1)
        await ctx.send(quotes[ind])

    @commands.command()
    async def morse(self, ctx, *sentence):
        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}
        res = ""
        for word in sentence:
            for char in word:
                res += MORSE_CODE_DICT[char.upper()]
                res += " "

        await ctx.send(res)

    @commands.command()
    async def demorse(self, ctx, *sentence):
        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}
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
        anime_gifs = ["https://tenor.com/view/anime-chainsaw-loli-girl-mad-gif-10166732",
                      "https://tenor.com/view/anime-gif-10117765",
                      "https://tenor.com/view/blush-anime-shy-cute-girl-gif-16149781",
                      "https://tenor.com/view/cute-anime-dancing-silly-happy-excited-gif-13462237",
                      "https://tenor.com/view/smug-anime-face-gif-6194051",
                      "https://tenor.com/view/laugh-anime-chuckle-gif-10903422",
                      "https://tenor.com/view/llorar1-cry-sad-tears-anime-gif-5648908",
                      "https://tenor.com/view/anime-love-lets-party-feel-the-love-throw-gif-13352944",
                      "https://tenor.com/view/anime-girl-phone-sad-gif-12144903",
                      "https://tenor.com/view/sleep-resting-bed-rest-anime-gif-5469651",
                      "https://tenor.com/view/bite-anime-cute-gif-8259627",
                      "https://tenor.com/view/karma-anime-blush-boy-gif-14841901",
                      "https://tenor.com/view/anime-thats-right-youre-right-gif-6015959",
                      "https://tenor.com/view/sensual-wink-blush-anime-animation-gif-5628679",
                      "https://tenor.com/view/shy-anime-embarassed-girl-gif-15974488",
                      "https://tenor.com/view/chuunibyou-anime-kawaii-yes-gif-8215787",
                      "https://tenor.com/view/cry-sad-why-anime-himouto-gif-5298257",
                      "https://tenor.com/view/love-you-happy-anime-the-helpful-fox-senko-san-gif-14521920",
                      "https://tenor.com/view/anime-zero-two-darling-in-the-franxx-cute-smile-gif-14500398"]
        await ctx.send(anime_gifs[random.randint(0, len(anime_gifs) - 1)])
