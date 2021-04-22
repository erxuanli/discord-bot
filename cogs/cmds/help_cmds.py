import discord
from discord.ext import commands

from bot import get_prefix

class HelpCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, category: str = None):
        # --------------------- help [listing categories] ------------------------------
        if category is None:
            embed = discord.Embed(title="help",
                                  description="all command categories listed below",
                                  color=discord.Color.purple())
            embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")

            fields = [(f"**{get_prefix(self.client, ctx)}help general**", "help for all general commands", False),
                      (f"**{get_prefix(self.client, ctx)}help testing**", "help for all testing commands", False),
                      (f"**{get_prefix(self.client, ctx)}help vc**", "help for all vc commands", False),
                      (f"**{get_prefix(self.client, ctx)}help fun**", "help for all fun commands", False),
                      (f"**{get_prefix(self.client, ctx)}help math**", "help for all math commands", False),
                      (f"**{get_prefix(self.client, ctx)}help science**", "help for all science commands", False),
                      (f"**{get_prefix(self.client, ctx)}help dumb**", "help for all dumb commands", False),
                      (f"**{get_prefix(self.client, ctx)}help management**", "help for all management commands", False),
                      (f"**{get_prefix(self.client, ctx)}help ecosystem**", "help for all ecosystem commands", False),
                      (f"**{get_prefix(self.client, ctx)}help games**", "help for all games commands", False),
                      (f"**{get_prefix(self.client, ctx)}help other**", "help for all other commands", False)]  

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)      
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help general ---------------------------------
        elif category == "general":
            embed = discord.Embed(title="help [general]",
                                  description="help for all general commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}creator**", "creator of this useless bot", False),
                      (f"**{get_prefix(self.client, ctx)}prefix**", "returns the current prefix", False),
                      (f"**{get_prefix(self.client, ctx)}avatar [user]**", "returns the avatar of the mentioned user", False),
                      (f"**{get_prefix(self.client, ctx)}savatar**", "returns the server icon", False),
                      (f"**{get_prefix(self.client, ctx)}clear [int]**", "clears channel [max 30]; do not spam", False),
                      (f"**{get_prefix(self.client, ctx)}id [member]**", "returns the id of a member", False),
                      (f"**{get_prefix(self.client, ctx)}info [user]**", "info about an user", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)  

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help testing ---------------------------------
        elif category == "testing":
            embed = discord.Embed(title="help [testing]",
                                  description="help for all testing commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}ping [precision : int; default 0]**", "bot latency", False),
                      (f"**{get_prefix(self.client, ctx)}time**", "returns the current time (of host location)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help vc ---------------------------------------
        elif category == "vc":
            embed = discord.Embed(title="help [vc]",
                                  description="help for all vc commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}join**", "join vc", False),
                      (f"**{get_prefix(self.client, ctx)}leave**", "leave vc", False),
                      (f"**{get_prefix(self.client, ctx)}vcmute**", "mute all in vc", False),
                      (f"**{get_prefix(self.client, ctx)}vcunmute**", "unmute all in vc", False),
                      (f"**{get_prefix(self.client, ctx)}play [url]**", "plays a mp3 file", False),
                      (f"**{get_prefix(self.client, ctx)}playl**", "plays the previous played mp3 file", False),
                      (f"**{get_prefix(self.client, ctx)}pause**", "pauses the current playing mp3 file", False),
                      (f"**{get_prefix(self.client, ctx)}resume**", "resumes the paused mp3 file", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help fun -------------------------------------
        elif category == "fun":
            embed = discord.Embed(title="help [fun]",
                                  description="help for all fun commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}quote**", "returns random quote", False),
                      (f"**{get_prefix(self.client, ctx)}ascii**", "converts to ascii / unicode", False),
                      (f"**{get_prefix(self.client, ctx)}ranimegif**", "random anime gif", False),
                      (f"**{get_prefix(self.client, ctx)}morse**", "converts to morse code", False),
                      (f"**{get_prefix(self.client, ctx)}demorse**", "converts morse code back", False),
                      (f"**{get_prefix(self.client, ctx)}note [your note]**", "saving a note", False),
                      (f"**{get_prefix(self.client, ctx)}rnote**", "read your created note", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help math -----------------------------------
        elif category == "math":
            embed = discord.Embed(title="help [math]",
                                  description="help for all math commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}sqfunc**", "returns zero points of a quadratic function", False),
                      (f"**{get_prefix(self.client, ctx)}pi**", "returns pi", False),
                      (f"**{get_prefix(self.client, ctx)}dice [min] [max]**", "random number", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # -------------------------- help science -------------------------------
        elif category == "science":            

            embed = discord.Embed(title="help [science]",
                                  description="help for all science commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}satellite [quan : int; default 1]**", "returns r and v of quan satellites now", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help dumb ----------------------------------
        elif category == "dumb":
            embed = discord.Embed(title="help [dumb]",
                                  description="help for all dumb commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}sheeesh**", "completely useless cmd", False),
                      (f"**{get_prefix(self.client, ctx)}melih**", "completely useless cmd", False),
                      (f"**{get_prefix(self.client, ctx)}erxuan**", "completely useless cmd", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help management ---------------------------------
        elif category == "management":
            embed = discord.Embed(title="help [management]",
                                  description="help for all management commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}addrole [user] [role]**", "adds a role to an user", False),
                      (f"**{get_prefix(self.client, ctx)}remrole [user] [role]**", "removes a role from an user", False),
                      (f"**{get_prefix(self.client, ctx)}kick [user] [reason]**", "kicks a member", False),
                      (f"**{get_prefix(self.client, ctx)}ban [user] [reason]**", "bans a member", False),
                      (f"**{get_prefix(self.client, ctx)}unban [user]**", "unbans a member", False),
                      (f"**{get_prefix(self.client, ctx)}nickname [user] [nickname]**", "changes the nickname of an user", False),
                      (f"**{get_prefix(self.client, ctx)}nicknames [nickname]**", "changes all nicknames", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help ecosystem ---------------------------------
        elif category == "ecosystem":
            embed = discord.Embed(title="help [ecosystem]",
                                  description="help for all ecosystem commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}daily**", "collect your daily money", False),
                      (f"**{get_prefix(self.client, ctx)}transfer [user] [amount]**", "transfer your given amount of money to another user", False),
                      (f"**{get_prefix(self.client, ctx)}wallet**", "shows how much money you have", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help games ----------------------------------
        elif category == "games":
            embed = discord.Embed(title="help [games]",
                                  description="help for all games",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}tictactoe [player1] [player2]**", "tic tac toe game (still in development)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help other ---------------------------------
        elif category == "other":
            embed = discord.Embed(title="help [other]",
                                  description="help for all other commands",
                                  color=discord.Color.blue())

            fields = [(f"**{get_prefix(self.client, ctx)}nicktimer [int : minutes]**", "start a nickname timer", False),
                      (f"**{get_prefix(self.client, ctx)}nicktimer_add [int : minutes]**", "add time to timer", False),
                      (f"**{get_prefix(self.client, ctx)}nicktimer_stop**", "stop running timer", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ------------------------- not a category ------------------------------------
        else:
            await ctx.send("That category is not available")
