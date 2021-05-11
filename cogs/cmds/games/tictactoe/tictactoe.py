import discord
from discord.ext import commands
import random

from cogs.cmds.custom_checks import not_in_blacklist
class TictactoeCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.player1 = None 
        self.player2 = None 
        self.turn = None 
        self.gameOver = False 
        self.count = 0
        self.board = []

        self.winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    @commands.command()
    @commands.check(not_in_blacklist)
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):

        self.board = [":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:",
                        ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:"]

        self.player1 = p1
        self.player2 = p2


        # prints board
        line = ""
        for x in range(len(self.board)):
            if (x+1) % 3 == 0:
                line += " " + self.board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + self.board[x]

        rand = random.randint(1, 2)
        if rand == 1:
            self.turn = self.player1
            await ctx.send(f"It is {self.player1.mention}'s turn.' ")
        elif rand == 2:
            self.turn = self.player2
            await ctx.send(f"It is {self.player2.mention}'s turn.")
        

    @commands.command()
    @commands.check(not_in_blacklist)
    async def place(self, ctx, pos: int):
        self.pos = pos

        if not self.gameOver:
            if self.turn == ctx.author:
                if self.turn == self.player1:
                    mark = ":regional_indicator_x:"
                elif self.turn == self.player2:
                    mark = ":o2:"
                if 0 < pos < 10 and self.board[pos - 1] == ":white_large_square:":
                    self.board[pos - 1] = mark
                    self.count += 1

                    line = ""
                    for x in range(len(self.board)):
                        if (x+1) % 3 == 0:
                            line += " " + self.board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + self.board[x]

                    
                    self.checkWinner(mark)
                    if self.gameOver == True:
                        await ctx.send(f"{ctx.author} ({mark}) wins!")
                    elif self.count >= 9:
                        self.gameOver = True
                        await ctx.send("It's a tie!")

                    if self.turn == self.player1:
                        self.turn = self.player2
                    elif self.turn == self.player2:
                        self.turn = self.player1

                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("Please wait your turn to play.")
        else:
            await ctx.send(f"Please start a new game using the {self.client.command_prefix(self.client, ctx)}tictactoe command.")

    def checkWinner(self, mark):
        for condition in self.winningConditions:
            if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[condition[2]] == mark:
                self.gameOver = True
