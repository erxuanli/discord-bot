import discord
from discord.ext import commands

from cogs.cmds.custom_checks import not_in_blacklist

class HelpCmds(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.footer_message = "our website: https://chi-discord-bot.github.io/"

    @commands.command()
    @commands.check(not_in_blacklist)
    async def help(self, ctx, category: str = None):
        cmd_prefix = self.client.command_prefix(self.client, ctx)[2]
        # --------------------- help [listing categories] ------------------------------
        if category is None:
            embed = discord.Embed(title="help",
                                  description="all command categories listed below",
                                  color=discord.Color.purple())
            embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")

            fields = [(f"**{cmd_prefix}help general**", "help for all general commands", False),
                      (f"**{cmd_prefix}help testing**", "help for all testing commands", False),
                      (f"**{cmd_prefix}help vc**", "help for all vc commands", False),
                      (f"**{cmd_prefix}help stats**", "help for all stats commands", False),
                      (f"**{cmd_prefix}help fun**", "help for all fun commands", False),
                      (f"**{cmd_prefix}help math**", "help for all math commands", False),
                      (f"**{cmd_prefix}help science**", "help for all science commands", False),
                      (f"**{cmd_prefix}help dumb**", "help for all dumb commands", False),
                      (f"**{cmd_prefix}help management**", "help for all management commands", False),
                      (f"**{cmd_prefix}help ecosystem**", "help for all ecosystem commands", False),
                      (f"**{cmd_prefix}help games**", "help for all games commands", False),
                      (f"**{cmd_prefix}help other**", "help for all other commands", False),
                      (f"**{cmd_prefix}help dev**", "help for all dev commands", False),
                      (f"**Like the bot? Invite me to your server!**", "https://discord.com/api/oauth2/authorize?client_id=825423193694797834&permissions=8&scope=bot", False),
                      (f"**Our website**", "https://chi-discord-bot.github.io/", False)]  

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)      
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help general ---------------------------------
        elif category == "general":
            embed = discord.Embed(title="help [general]",
                                  description="help for all general commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}creator**", "creator of this useless bot", False),
                      (f"**{cmd_prefix}prefix**", "returns the current prefix", False),
                      (f"**{cmd_prefix}avatar [user]**", "returns the avatar of the mentioned user", False),
                      (f"**{cmd_prefix}savatar**", "returns the server icon", False),
                      (f"**{cmd_prefix}clear [int]**", "clears channel [max 30]; do not spam", False),
                      (f"**{cmd_prefix}id [member]**", "returns the id of a member", False),
                      (f"**{cmd_prefix}info [user]**", "info about an user", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline)  

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help testing ---------------------------------
        elif category == "testing":
            embed = discord.Embed(title="help [testing]",
                                  description="help for all testing commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}ping [precision : int; default 0]**", "bot latency", False),
                      (f"**{cmd_prefix}time**", "returns the current time (of host location)", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help vc ---------------------------------------
        elif category == "vc":
            embed = discord.Embed(title="help [vc]",
                                  description="help for all vc commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}join**", "join vc", False),
                      (f"**{cmd_prefix}leave**", "leave vc", False),
                      (f"**{cmd_prefix}vcmute**", "mute all in vc", False),
                      (f"**{cmd_prefix}vcunmute**", "unmute all in vc", False),
                      (f"**{cmd_prefix}play [url]**", "plays a mp3 file", False),
                      (f"**{cmd_prefix}playl**", "plays the previous played mp3 file", False),
                      (f"**{cmd_prefix}pause**", "pauses the current playing mp3 file", False),
                      (f"**{cmd_prefix}resume**", "resumes the paused mp3 file", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help stats ---------------------------------------
        elif category == "stats":
            embed = discord.Embed(title="help [stats]",
                                  description="help for all stats commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}vcstats [user; default: message author]**", "returns vc stats of an user", False),
                      (f"**{cmd_prefix}vctop [lookback days; default: all time]**", "top 10 vc users", False),
                      (f"**{cmd_prefix}vctopglobal [lookback days; default: all time]**", "top 10 vc users (global)", False),
                      (f"**{cmd_prefix}vctopserver [lookback days; default: all time]**", "top 10 vc servers", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help fun -------------------------------------
        elif category == "fun":
            embed = discord.Embed(title="help [fun]",
                                  description="help for all fun commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}quote**", "returns random quote", False),
                      (f"**{cmd_prefix}ascii**", "converts to ascii / unicode", False),
                      (f"**{cmd_prefix}ranimegif**", "random anime gif", False),
                      (f"**{cmd_prefix}morse**", "converts to morse code", False),
                      (f"**{cmd_prefix}demorse**", "converts morse code back", False),
                      (f"**{cmd_prefix}note [your note]**", "saving a note", False),
                      (f"**{cmd_prefix}rnote**", "read your created note", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help math -----------------------------------
        elif category == "math":
            embed = discord.Embed(title="help [math]",
                                  description="help for all math commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}sqfunc**", "returns zero points of a quadratic function", False),
                      (f"**{cmd_prefix}pi**", "returns pi", False),
                      (f"**{cmd_prefix}dice [min] [max]**", "random number", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # -------------------------- help science -------------------------------
        elif category == "science":            

            embed = discord.Embed(title="help [science]",
                                  description="help for all science commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}satellite [quan : int; default 1]**", "returns r and v of quan satellites now", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help dumb ----------------------------------
        elif category == "dumb":
            embed = discord.Embed(title="help [dumb]",
                                  description="help for all dumb commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}sheeesh**", "completely useless cmd", False),
                      (f"**{cmd_prefix}melih**", "completely useless cmd", False),
                      (f"**{cmd_prefix}erxuan**", "completely useless cmd", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help management ---------------------------------
        elif category == "management":
            embed = discord.Embed(title="help [management]",
                                  description="help for all management commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}addrole [user] [role]**", "adds a role to an user", False),
                      (f"**{cmd_prefix}remrole [user] [role]**", "removes a role from an user", False),
                      (f"**{cmd_prefix}kick [user] [reason]**", "kicks a member", False),
                      (f"**{cmd_prefix}ban [user] [reason]**", "bans a member", False),
                      (f"**{cmd_prefix}unban [user]**", "unbans a member", False),
                      (f"**{cmd_prefix}nickname [user] [nickname]**", "changes the nickname of an user", False),
                      (f"**{cmd_prefix}nicknames [nickname]**", "changes all nicknames", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 

            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help ecosystem ---------------------------------
        elif category == "ecosystem":
            embed = discord.Embed(title="help [ecosystem]",
                                  description="help for all ecosystem commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}daily**", "collect your daily money", False),
                      (f"**{cmd_prefix}transfer [user] [amount]**", "transfer your given amount of money to another user", False),
                      (f"**{cmd_prefix}wallet**", "shows how much money you have", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help games ----------------------------------
        elif category == "games":
            embed = discord.Embed(title="help [games]",
                                  description="help for all games",
                                  color=discord.Color.blue())

            fields = [(f"**nothing here yet**", "404 xD", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ---------------------------- help other ---------------------------------
        elif category == "other":
            embed = discord.Embed(title="help [other]",
                                  description="help for all other commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}nicktimer [int : minutes]**", "start a nickname timer", False),
                      (f"**{cmd_prefix}nicktimer_add [int : minutes]**", "add time to timer", False),
                      (f"**{cmd_prefix}nicktimer_stop**", "stop running timer", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # --------------------------- help dev --------------------------------------
        elif category == "dev":
            embed = discord.Embed(title="help [dev]",
                                  description="help for all dev commands",
                                  color=discord.Color.blue())

            fields = [(f"**{cmd_prefix}vcsj**", "returns json file of user vc stats", False),
                      (f"**{cmd_prefix}debug**", "disable all cmds", False),
                      (f"**{cmd_prefix}broadcast [message]**", "sending message to all general channels", False)]

            for name, value, inline in fields:
                embed.add_field(name = name, value = value, inline = inline) 
            
            embed.set_footer(text=self.footer_message)

            await ctx.send(embed=embed)

        # ------------------------- not a category ------------------------------------
        else:
            await ctx.send("That category is not available")
