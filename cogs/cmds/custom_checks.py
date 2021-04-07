import os

def is_creator(ctx):
    # erxuan = int(os.environ['MY_DISCORD_ID'])
    # melih = 237150657184923649 
    # if melih == ctx.author.id or erxuan == ctx.author.id:
    #     return True

    return ctx.author.id == int(os.environ['MY_DISCORD_ID'])
