import discord
import os
import random
from discord.ext import commands


class database(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Database ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = str.lower(message.content) # semi-redundant
        if message.author.bot:
            return
        if not message.content:
            return
        if msg[0] == "-": # make sure its not a command 
            return
        if "waf" in msg:
            return
        if message.mentions:
            return
        for channel in message.guild.text_channels:
                if channel.is_nsfw():
                    pass
        data = 'data/' + f"{message.guild.id}" + '.txt.' # find server folder and channel file
        if os.path.exists(data): # it exists? awesome write a new line to it
            file = open(data, 'a')
            file.write(f"{message.channel.id}-{message.id}" + "\n")
            #print(f"{message.id}" + " to " + data)
            file.close
        else: #file doesn't exist? that sucks, make it
            fp = open(data, 'x')
            fp.close()
            print("created new file: " + data)

    @commands.command()
    async def filldb(self, ctx):
        ID = 146395257313951744
        if ctx.author.id == ID:
            if ctx.author == self.client.user:
                return
            if ctx.author.bot:
                return
            async with ctx.channel.typing():
                for chnl in ctx.guild.text_channels:
                    try:
                        if chnl.is_nsfw() or not ctx.message.content:
                            pass
                        async for msgholder in chnl.history(limit=None):
                            if not msgholder.content or msgholder.content[0] == "-" or msgholder.author.bot or msgholder.mentions:
                                continue
                            data = 'data/' + f"{ctx.guild.id}" + '.txt.' # find server folder and channel file
                            if os.path.exists(data): # it exists? awesome write a new line to it
                                file = open(data, 'a')
                                file.write(f"{msgholder.channel.id}-{msgholder.id}" + "\n")
                                file.close
                            else: #file doesn't exist? that sucks, make it
                                fp = open(data, 'x')
                                fp.close()
                    except:
                        pass
            await ctx.channel.send(f'filled database') 
            if ctx.author.id != ID:
                await ctx.channel.send('no')
                return


    @commands.command()
    async def cleardb(self, ctx):
        ID = 146395257313951744
        if ctx.author.id == ID:
            if ctx.author == self.client.user:
                return
            data = 'data/' + f"{ctx.guild.id}" + '.txt.' # find server folder and channel file
            if os.path.exists(data): # it exists? awesome write a new line to it
                file = open(data, 'w')
                file.close()
                await ctx.channel.send(f'cleared database')
        if ctx.author.id != ID:
            await ctx.channel.send('no')
            return

def setup(client):
    client.add_cog(database(client))