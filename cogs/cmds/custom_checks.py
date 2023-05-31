import os

def is_creator(ctx):
    return ctx.author.id == 538375186722979851

def is_flori(ctx):
    return (ctx.author.id == 681969539935633441 or ctx.author.id == 1113208509157347368)

def is_moderator(ctx):
    if ctx.author.id == 237150657184923649 or ctx.author.id == 751084480097157251 or ctx.author.id == 538375186722979851:
        return True

def not_in_blacklist(ctx):
    blacklist = []
    if ctx.author.id not in blacklist:
        return True
    return False

