import discord
from discord.ext import commands


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

            fields = [(f"**{self.client.command_prefix}help general**", "help for all general commands", False),
                      (f"**{self.client.command_prefix}help testing**", "help for all testing commands", False),
                      (f"**{self.client.command_prefix}help vc**", "help for all vc commands", False),
                      (f"**{self.client.command_prefix}help fun**", "help for all fun commands", False),
                      (f"**{self.client.command_prefix}help math**", "help for all math commands", False),
                      (f"**{self.client.command_prefix}help science**", "help for all science commands", False),
                      (f"**{self.client.command_prefix}help dumb**", "help for all dumb commands", False),
                      (f"**{self.client.command_prefix}help management**", "help for all management commands", False),
                      (f"**{self.client.command_prefix}help ecosystem**", "help for all ecosystem commands", False),
                      (f"**{self.client.command_prefix}help games**", "help for all games commands", False),
                      (f"**{self.client.command_prefix}help other**", "help for all other commands", False)]  

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)      
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help general ---------------------------------
        elif category == "general":
            embed = discord.Embed(title="help [general]",
                                  description="help for all general commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}creator**", "creator of this useless bot", False),
                      (f"**{self.client.command_prefix}prefix**", "returns the current prefix", False),
                      (f"**{self.client.command_prefix}avatar [user]**", "returns the avatar of the mentioned user", False),
                      (f"**{self.client.command_prefix}clear [int]**", "clears channel [max 30]; do not spam", False),
                      (f"**{self.client.command_prefix}id [member]**", "returns the id of a member", False),
                      (f"**{self.client.command_prefix}info [user]**", "info about an user", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)  

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help testing ---------------------------------
        elif category == "testing":
            embed = discord.Embed(title="help [testing]",
                                  description="help for all testing commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}ping [precision : int; default 0]**", "bot latency", False),
                      (f"**{self.client.command_prefix}time**", "returns the current time (of host location)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help vc ---------------------------------------
        elif category == "vc":
            embed = discord.Embed(title="help [vc]",
                                  description="help for all vc commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}join**", "join vc", False),
                      (f"**{self.client.command_prefix}leave**", "leave vc", False),
                      (f"**{self.client.command_prefix}vcmute**", "mute all in vc", False),
                      (f"**{self.client.command_prefix}vcunmute**", "unmute all in vc", False),
                      (f"**{self.client.command_prefix}play [url]**", "plays a mp3 file", False),
                      (f"**{self.client.command_prefix}playl**", "plays the previous played mp3 file", False),
                      (f"**{self.client.command_prefix}pause**", "pauses the current playing mp3 file", False),
                      (f"**{self.client.command_prefix}resume**", "resumes the paused mp3 file", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help fun -------------------------------------
        elif category == "fun":
            embed = discord.Embed(title="help [fun]",
                                  description="help for all fun commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}quote**", "returns random quote", False),
                      (f"**{self.client.command_prefix}ascii**", "converts to ascii / unicode", False),
                      (f"**{self.client.command_prefix}ranimegif**", "random anime gif", False),
                      (f"**{self.client.command_prefix}morse**", "converts to morse code", False),
                      (f"**{self.client.command_prefix}demorse**", "converts morse code back", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help math -----------------------------------
        elif category == "math":
            embed = discord.Embed(title="help [math]",
                                  description="help for all math commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}sqfunc**", "returns zero points of a quadratic function", False),
                      (f"**{self.client.command_prefix}pi**", "returns pi", False),
                      (f"**{self.client.command_prefix}dice [min] [max]**", "random number", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # -------------------------- help science -------------------------------
        elif category == "science":            

            embed = discord.Embed(title="help [science]",
                                  description="help for all science commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}satellite [quan : int; default 1]**", "returns r and v of quan satellites now", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help dumb ----------------------------------
        elif category == "dumb":
            embed = discord.Embed(title="help [dumb]",
                                  description="help for all dumb commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}sheeesh**", "completely useless cmd", False),
                      (f"**{self.client.command_prefix}melih**", "completely useless cmd", False),
                      (f"**{self.client.command_prefix}erxuan**", "completely useless cmd", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help management ---------------------------------
        elif category == "management":
            embed = discord.Embed(title="help [management]",
                                  description="help for all management commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}addrole [user] [role]**", "adds a role to an user", False),
                      (f"**{self.client.command_prefix}remrole [user] [role]**", "removes a role from an user", False),
                      (f"**{self.client.command_prefix}kick [user] [reason]**", "kicks a member", False),
                      (f"**{self.client.command_prefix}ban [user] [reason]**", "bans a member", False),
                      (f"**{self.client.command_prefix}unban [user]**", "unbans a member", False),
                      (f"**{self.client.command_prefix}nickname [user] [nickname]**", "changes the nickname of an user", False),
                      (f"**{self.client.command_prefix}nicknames [nickname]**", "changes all nicknames", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help ecosystem ---------------------------------
        elif category == "ecosystem":
            embed = discord.Embed(title="help [ecosystem]",
                                  description="help for all ecosystem commands",
                                  color=discord.Color.blue())

            fields = [(f"**404**", "nothing here yet", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help games ----------------------------------
        elif category == "games":
            embed = discord.Embed(title="help [games]",
                                  description="help for all games",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}tictactoe [player1] [player2]**", "tic tac toe game (still in development)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help other ---------------------------------
        elif category == "other":
            embed = discord.Embed(title="help [other]",
                                  description="help for all other commands",
                                  color=discord.Color.blue())

            fields = [(f"**{self.client.command_prefix}nicktimer [int : minutes]**", "a nickname timer (still in development)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ------------------------- not a category ------------------------------------
        else:
            await ctx.send("That category is not available")
