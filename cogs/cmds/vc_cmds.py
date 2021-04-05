import discord
from discord.ext import commands

import os
import youtube_dl


class VcCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel}")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()
            await ctx.send(f"Disconnected from {ctx.voice_client}")
        else:
            await ctx.send("Bot is not in a voice channel")

    @commands.command()
    async def vcmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=True)
        await ctx.send(f"Muted all members in {vc}")

    @commands.command()
    async def vcunmute(self, ctx):
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)
        await ctx.send(f"Unmuted all members in {vc}")

    @commands.command()
    async def play(self, ctx, url: str):
        audio_there = os.path.isfile("audio.mp3")
        try:
            if audio_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Currently playing")
        channel = ctx.author.voice.channel
        if not channel.is_connected():
            await channel.connect()
            await ctx.send(f"Joined {channel}")

        ydl_opts = {"format": "bestaudio/best",
                    "postprocessors": [{"key": "FFmpegExtractAudio",
                                        "preferredcodec": "mp3",
                                        "preferredquality": "192"
                                        }]
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        channel.play(discord.FFmpegAudio("audio.mp3"))

    @commands.command()
    async def pause(self, ctx):
        channel = ctx.author.voice.channel
        if channel.is_playing():
            channel.pause()
        else:
            await ctx.send("Nothing playing right now")

    @commands.command()
    async def resume(self, ctx):
        channel = ctx.author.voice.channel
        if channel.is_paused():
            channel.resume()
        else:
            await ctx.send("Nothing paused")

    @commands.command()
    async def stop(self, ctx):
        channel = ctx.author.voice.channel
        channel.stop()
