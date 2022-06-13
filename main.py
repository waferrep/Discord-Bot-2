import os
import discord
from discord.ext import commands

TOKEN = #YOUR TOKEN HERE
ID = 146395257313951744

client = commands.Bot(command_prefix='-')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def load(ctx, extension):
    if ctx.author.id == ID:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} loaded.')
    if ctx.author.id != ID:
        await ctx.send('no')


@client.command()
async def unload(ctx, extension, avamember : discord.Member=None):
    if ctx.author.id == ID:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} unloaded.')
    if ctx.author.id != ID:
        await ctx.send('no')

client.run(TOKEN)
