import discord
from discord.ext import commands

import os
import youtube_dl


class VcCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel")
            return 
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel}")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Bot is not in a voice channel")
        elif ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()
            await ctx.send(f"Disconnected")

    @commands.command(aliases = ["vm"])
    async def vcmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=True)
        await ctx.send(f"Muted all members in {vc}")

    @commands.command(aliases = ["vu"])
    async def vcunmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)
        await ctx.send(f"Unmuted all members in {vc}")

    @commands.command(aliases = ["p"])
    async def play(self, ctx, url: str):
        # ------------ check user vc connection -------------------
        if ctx.message.author.voice is None:
            await ctx.send("Please join a voice channel")
            return

        # ------------ downloading mp3 ---------------------------
        await ctx.send("Downloading mp3 || Please wait")
        audio_there = os.path.isfile(f"./cogs/cmds/cmd_utils/music_audio_files/{ctx.guild.id}.mp3")
        try:
            if audio_there:
                os.remove(f"./cogs/cmds/cmd_utils/music_audio_files/{ctx.guild.id}.mp3")
        except PermissionError:
            await ctx.send("Currently playing")

        ydl_opts = {"format": "bestaudio/best",
                    "postprocessors": [{"key": "FFmpegExtractAudio",
                                        "preferredcodec": "mp3",
                                        "preferredquality": "192"
                                        }],
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, f"./cogs/cmds/cmd_utils/music_audio_files/{ctx.guild.id}.mp3")

        # --------------- check bot vc connection ---------------
        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        # --------------- play mp3 ----------------------------
        source = discord.FFmpegPCMAudio(f"./cogs/cmds/cmd_utils/music_audio_files/{ctx.guild.id}.mp3")
        voice.play(source)
        await ctx.send("Playing mp3")

    @commands.command(aliases = ["pl"])
    async def playl(self, ctx):
        # ------------ check user vc connection -------------------
        if ctx.message.author.voice is None:
            await ctx.send("Please join a voice channel")
            return
        channel = ctx.message.author.voice.channel        
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = discord.FFmpegPCMAudio(f"./cogs/cmds/cmd_utils/music_audio_files/{ctx.guild.id}.mp3")
        voice.play(source)
        await ctx.send("Playing mp3")
    
   
