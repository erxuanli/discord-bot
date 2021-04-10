import discord
from discord.ext import commands


class ErrorHandlerCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument(s). Please search this command with {self.client.command_prefix}help and check which arguments are required.")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"That command is not available. You can check all available commands with {self.client.command_prefix}help.")

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("This command can not be used in private messages. Please head over to a discord server.")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Access denied")

        else:
            await ctx.send("Whoops. Something went wrong...")
            await ctx.send(error)

