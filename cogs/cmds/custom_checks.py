import os

def is_creator(ctx):
    return ctx.author.id == int(os.environ['MY_DISCORD_ID'])

    
