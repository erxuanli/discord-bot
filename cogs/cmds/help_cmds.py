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
            embed.set_thumbnail(
                url="https://static.wikia.nocookie.net/the-muse-list/images/f/fd/Albedo_Pout.jpg")

            embed.add_field(name=f"**{self.client.command_prefix}help general**",
                            value="help for all general commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help testing**",
                            value="help for all testing commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help vc**",
                            value="help for all vc commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help fun**",
                            value="help for all fun commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help math**",
                            value="help for all math commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help dumb**",
                            value="help for all dumb commands", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}help management**",
                            value="help for all management commands", inline=False)

            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help general ---------------------------------
        elif category == "general":
            embed = discord.Embed(title="help [general]",
                                  description="help for all general commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}creator**",
                            value="creator of this useless bot", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}prefix**",
                            value="returns the current prefix", inline=False)
            embed.add_field(
                name=f"**{self.client.command_prefix}avatar [user]**", value="returns the avatar of the mentioned user", inline=False)
            embed.add_field(
                name=f"**{self.client.command_prefix}clear [int]**", value="clears channel [max 30]; do not spam", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help testing ---------------------------------
        elif category == "testing":
            embed = discord.Embed(title="help [testing]",
                                  description="help for all testing commands",
                                  color=discord.Color.blue())
            embed.add_field(
                name=f"**{self.client.command_prefix}ping**", value="bot latency", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}time**",
                            value="returns the current time (of host location)", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help vc ---------------------------------------
        elif category == "vc":
            embed = discord.Embed(title="help [vc]",
                                  description="help for all vc commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}join**",
                            value="join vc", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}leave**",
                            value="leave vc", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}vcmute**",
                            value="mute all in vc", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}vcunmute**",
                            value="unmute all in vc", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}play [url]**",
                            value="plays a mp3 file", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}playl**",
                            value="plays the previous played mp3 file", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help fun -------------------------------------
        elif category == "fun":
            embed = discord.Embed(title="help [fun]",
                                  description="help for all fun commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}quote**",
                            value="returns random quote", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}ascii**",
                            value="converts to ascii / unicode", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}ranimegif**",
                            value="random anime gif", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}morse**",
                            value="converts to morse code", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}demorse**",
                            value="converts morse code back", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help math -----------------------------------
        elif category == "math":
            embed = discord.Embed(title="help [math]",
                                  description="help for all math commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}sqfunc**",
                            value="returns zero points of a quadratic function", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}pi**", value="returns pi", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}dice [min] [max]**",
                            value="random number", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help dumb ----------------------------------
        elif category == "dumb":
            embed = discord.Embed(title="help [dumb]",
                                  description="help for all dumb commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}sheeesh**",
                            value="completely useless cmd", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}melih**",
                            value="completely useless cmd", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)

        # ---------------------------- help management ---------------------------------
        elif category == "management":
            embed = discord.Embed(title="help [management]",
                                  description="help for all management commands",
                                  color=discord.Color.blue())
            embed.add_field(name=f"**{self.client.command_prefix}addrole [user] [role]**",
                            value="adds a role to an user", inline=False)
            embed.add_field(name=f"**{self.client.command_prefix}remrole [user] [role]**",
                            value="removes a role from an user", inline=False)
            embed.set_footer(
                text="Thanks for using this useless bot xD and greetings to all weebs xD")

            await ctx.send(embed=embed)




   
