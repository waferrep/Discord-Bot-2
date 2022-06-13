from logging import exception
import discord
from discord.ext import commands
import aiohttp

class api(commands.Cog):

    def __init__(self, client):
        self.client = client

    try:
        from googlesearch import search 
    except ImportError:
        print("No module found!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/red_panda')
            pogjson = await request.json()
        embed = discord.Embed(title="red panda", color=discord.Color.red())
        embed.set_image(url=pogjson['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
        embed = discord.Embed(title="dog", color=discord.Color.green())
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def birb(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/birb')
            birdjson = await request.json()
        embed = discord.Embed(title="birb", color=discord.Color.blue())
        embed.set_image(url=birdjson['link'])
        await ctx.send(embed=embed)    

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()
        embed = discord.Embed(title="cat", color=discord.Color.teal())
        embed.set_image(url=catjson['link'])
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(api(client))