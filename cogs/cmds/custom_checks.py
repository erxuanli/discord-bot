import os

def is_creator(ctx):
    return ctx.author.id == int(os.environ['MY_DISCORD_ID'])

def is_flori(ctx):
    return ctx.author.id == 751084480097157251
