import discord
from discord.ext import commands

import random
import datetime
import math

# import keep_alive

import pi_num

client = commands.Bot(command_prefix=";", help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=";help || Stalking PolarBear4u#7025"))
    print(f"{client.user}: Connected")


# ---------------------- general commands -----------------------------------
@client.command()
async def creator(ctx):
    await ctx.send("PolarBear4u sennnnpaiiiiii")


@client.command()
async def help(ctx):
    embed = discord.Embed(title="help",
                          description="all useless cmds are listed below",
                          color=discord.Color.purple())
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")
    embed.add_field(name="**;help**",
                    value="That's this command xD", inline=False)
    embed.add_field(name="**;creator**",
                    value="creator of this useless bot", inline=False)
    embed.add_field(name="**;prefix**",
                    value="returns the current prefix", inline=False)
    embed.add_field(
        name="**;avatar [user]**", value="returns the avatar of the mentioned user", inline=False)
    embed.add_field(
        name="**;clear [int]**", value="clears channel [max 30]; do not spam", inline=False)
    embed.add_field(name="**;ping**", value="bot latency", inline=False)
    embed.add_field(name="**;time**",
                    value="returns the current time (of host location)", inline=False)
    embed.add_field(name="**;join**",
                    value="join vc", inline=False)
    embed.add_field(name="**;leave**",
                    value="leave vc", inline=False)
    embed.add_field(name="**;quote**",
                    value="returns random quote", inline=False)
    embed.add_field(name="**;ascii**",
                    value="converts to ascii / unicode", inline=False)
    embed.add_field(name="**;ranimegif**",
                    value="random anime gif", inline=False)
    embed.add_field(name="**;morse**",
                    value="converts to morse code", inline=False)
    embed.add_field(name="**;demorse**",
                    value="converts morse code back", inline=False)
    embed.add_field(name="**;sqfunc**",
                    value="returns zero points of a quadratic function", inline=False)
    embed.add_field(name="**;pi**", value="returns pi", inline=False)
    embed.add_field(name="**;dice [min] [max]**",
                    value="random number", inline=False)
    embed.add_field(name="**;sheeesh**",
                    value="completely useless cmd", inline=False)
    embed.add_field(name="**;melih**",
                    value="completely useless cmd", inline=False)
    embed.set_footer(
        text="Thanks for using this useless bot xD and greetings to all weebs xD")

    await ctx.send(embed=embed)


@client.command()
async def prefix(ctx):
    await ctx.send(client.command_prefix)


@client.command()
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(ctx.author.avatar_url)
    else:
        userAvatarUrl = user.avatar_url
        await ctx.send(userAvatarUrl)


@client.command()
async def clear(ctx, amount=5):
    if amount > 30:
        await ctx.send("max amount 30")
    else:
        await ctx.channel.purge(limit=amount)

# ---------------------- testing commands ----------------------------------


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def time(ctx):
    await ctx.send(datetime.datetime.now())

# ---------------------- vc commands -------------------------------------


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# --------------------- fun commands --------------------------------------


@client.command()
async def quote(ctx):
    quotes = ["“Be yourself; everyone else is already taken.” ― Oscar Wilde",
              "“I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.” ― Marilyn Monroe",
              "“Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.” ― Albert Einstein",
              "“So many books, so little time.” ― Frank Zappa",
              "“A room without books is like a body without a soul.” ― Marcus Tullius Cicero"]
    ind = random.randint(0, len(quotes) - 1)
    await ctx.send(quotes[ind])


@client.command()
async def morse(ctx, *sentence):
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


@client.command()
async def demorse(ctx, *sentence):
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


@client.command()
async def ascii(ctx, *sentence):
    res = ""
    for word in sentence:
        for char in word:
            res += str(ord(char))
            res += "/"
        res = res[:-1]
        res += " | "
    res = res[:-3]
    await ctx.send(res)


@client.command()
async def ranimegif(ctx):
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


# --------------------- math commands ----------------------------------------
@client.command()
async def sqfunc(ctx, a: float, b: float, c: float):
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


@client.command()
async def pi(ctx):
    await ctx.send(pi_num.pi_num)


@client.command()
async def dice(ctx, min, max):
    await ctx.send(random.randint(int(min), int(max)))


# --------------------- dumb and troll commands -----------------------------
@client.command()
async def sheeesh(ctx):
    await ctx.send("ruben cringemai 2.0?")


@client.command()
async def melih(ctx):
    await ctx.send("i'm gaaaaaayy xD")

# ----------------------- non cmd responses ----------------------------------


@client.event
async def on_message(message):

    # ---------------------- happy responses ---------------------------------
    if "happy birthday" in message.content.lower():
        await message.channel.send("Happpppyyyyyy Birrrthhhhdayyyy!!!")

    # ---------------------- troll flori resposes ----------------------------
    if message.content.startswith("mh"):
        await message.channel.send("troll")
    if message.content.startswith("ms"):
        await message.channel.send("troll")
    if message.content.startswith("mwork"):
        await message.channel.send("troll")
    if message.content.startswith("mcd"):
        await message.channel.send("troll")
    if message.content.startswith("mdaily"):
        await message.channel.send("troll")
    if message.content.startswith("mvote"):
        await message.channel.send("troll")
    if message.content.startswith("mbj"):
        await message.channel.send("troll")

    await client.process_commands(message)


# keep_alive.keep_alive()
client.run("ODI1NDIzMTkzNjk0Nzk3ODM0.YF9tQA.99TXXuF3hPpRgIPMdNMI-G63w4s")
