import discord
import os
import random
from discord.ext import commands

class dbpick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if "waf" in message.content.lower():
            async with message.channel.typing():
                file = 'data/' + f"{message.guild.id}.txt" # set directory for readability; search this directory for a random channel
                with open(file) as f: #open the file
                    file_lines = [line.rstrip() for line in f.readlines()] #idk. clean lines from \n i think
                    chosen = random.choice(file_lines) # pick a random message
                    picked_channel = chosen[0:18]
                    orgchannel = await self.client.fetch_channel(picked_channel) # lookup channel
                    message_to_send = await orgchannel.fetch_message(chosen[19:]) # lookup message
                    await message.channel.send(message_to_send.content) # send 

def setup(client):
    client.add_cog(dbpick(client))