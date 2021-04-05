import os

def is_polarbear(ctx):
    return ctx.author.id == os.environ['MY_DISCORD_ID']