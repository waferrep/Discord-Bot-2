import discord
from discord.ext import commands
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self): 
        print("Ready cog loaded") 

    #gets user info and then prints user info + msg to console
    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author).split('#')[0] 
        user_message = str(message.content)
        channel = str(message.channel.name) 
        print(f'{username}: {user_message} ({channel})') 

        if message.author == self.client.user:
            return
        
        randomGen1 = random.randrange(1, 6)
        #1/6 chance to repsond to one of these messages randomly
        if randomGen1 == 1:
            if "gm" in message.content.lower():
                await message.channel.send(f'GM {username}', reference=message)

            elif "gn" in message.content.lower():
                await message.channel.send(f'GN {username}', reference=message)
            
            elif "jinx" in message.content.lower()  or "cat" in message.content.lower():
                await message.channel.send('https://cdn.discordapp.com/attachments/754245502538743808/957467294156615680/9k.png')

            elif "dorchadas" in message.content.lower():
                await message.channel.send('https://media.discordapp.net/attachments/952203557724094525/957235469131874314/ezgif.com-gif-maker_2.gif')

            elif "kiby" in message.content.lower():
                await message.channel.send('https://tenor.com/view/kirby-kirby-cooked-kirby-massage-kirby-pat-massage-gif-25195626')

            elif "fish" in message.content.lower() or "fishing" in message.content.lower():
                await message.channel.send('https://cdn.discordapp.com/attachments/754245502538743808/958202794211414096/FO-32LgVUAMXEO-.png')

            elif "fire" in message.content.lower():
                emoji = '🔥'
                await message.add_reaction(emoji)

            elif "upvote" in message.content.lower():
                emoji = '<:upvote:957698832513237022>'
                await message.add_reaction(emoji)

            elif "downvote" in message.content.lower():
                emoji = '<:downvote:957699003863150602>'
                await message.add_reaction(emoji)

        #respond to user pinging the bot
        for x in message.mentions:
            if '-' in message.content[0]:
                return
            if (x==self.client.user):
                randomGen = random.randint(1, 3) 
                if randomGen == 1:
                    await message.channel.send(f"whatttttttttttttttt", reference=message)
                elif randomGen == 2:
                    await message.channel.send(f'<@!{message.author.id}>', reference=message)
                elif randomGen == 3:
                    await message.channel.send(f'stop pinging me!!!!!', reference=message)
                        
    @commands.command() #random # from this range, shld add userinput to determine range someday
    async def random(self, ctx):
        async with ctx.typing():
            await ctx.reply(random.randrange(100000))

    @commands.command() #test ping
    async def ping(self, ctx):
        async with ctx.typing():
            await ctx.reply(f'pong:  {round(self.client.latency * 1000)} ms')

    @commands.command() #8ball command
    async def yesno(self, ctx):
        async with ctx.typing():
            randomGen = random.randint(1, 6) 
            if randomGen == 1:
                await ctx.reply(f'no')
            elif randomGen == 2:
                await ctx.reply(f'yes')
            elif randomGen == 3:
                await ctx.reply(f'maybe')
            elif randomGen == 4:
                await ctx.reply(f'try again')
            elif randomGen == 5:
                await ctx.reply(f'absolutely')
            elif randomGen == 6:
                await ctx.reply(f'negative')

    @commands.command() #sends a users avatar
    async def ava(self, ctx, avamember : discord.Member=None):
        async with ctx.typing():
            userAvatarUrl = avamember.avatar_url
            await ctx.send(userAvatarUrl)


def setup(client):
    client.add_cog(fun(client))
