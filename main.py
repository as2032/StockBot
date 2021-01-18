import discord
from discord.ext import commands
import os
import stock
client = commands.Bot(command_prefix="$")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")




# class run(args):
#     print("im here")
#     stocklist = []
#     for i in range(len(args)):
#         stocklist.append(args[i])
#     outlist = runStonks(stocklist)
#     return outlist



@client.command(name="stonk")
async def stonk(ctx, *args) :
    out = stock.runStonks(args)
    await ctx.send(out)
    #await ctx.send('{} stocks in watchlist: {}'.format(len(args), ', '.join(args)))



@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")





@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)









# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
