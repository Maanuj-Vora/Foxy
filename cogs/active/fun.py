import os
import discord
from discord.ext import commands

import psutil
import random
import aiohttp
import asyncio
import requests
import time

from datetime import date, datetime
from utils import default, lists, embed

QUERY_EXCEPTIONS = None
QUERY_ERROR = None


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        global QUERY_EXCEPTIONS
        global QUERY_ERROR
        QUERY_EXCEPTIONS = (
            discord.HTTPException, aiohttp.ClientError, asyncio.TimeoutError, commands.CommandError)
        QUERY_ERROR = commands.CommandError(
            'Query failed. Try again later.')

    def urljson(url, headers):
        try:
            if(headers == None):
                response = requests.get(url)
            else:
                response = requests.get(url, headers=headers)
            if response.status_code != 200:
                raise QUERY_ERROR
            json = response.json()
            return json
        except QUERY_EXCEPTIONS:
            raise QUERY_ERROR

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult the supreme, all knowing 8ball to receive an answer """
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {random.choice(lists.ballresponse)}")

    @commands.command(aliases=['cn', 'cnjoke'])
    async def chucknorris(self, ctx):
        """ Get a Chuck Norris Joke """
        async with ctx.message.channel.typing():
            for x in range(0, 5):
                json = Fun.urljson('http://api.icndb.com/jokes/random', None)
                textLower = json['value'].get('joke').lower()
                if not any(map(textLower.__contains__, lists.profanity)):
                    await embed.embedText(ctx, json['value'].get('joke'))
                    return
            await embed.embedText(ctx, 'Could not find a PG Chuck Norris Joke')
            return

    @commands.command(aliases=['rs', 'rsquote'])
    async def ronswanson(self, ctx):
        """ Get a Ron Swanson Quote """
        try:
            json = Fun.urljson(
                'http://ron-swanson-quotes.herokuapp.com/v2/quotes', None)
            await embed.embedText(ctx, 'Ron Swanson Says', json[0])
            return
        except Exception as e:
            await ctx.send("An Error Occured")
            return

    @commands.command()
    async def bored(self, ctx):
        """ Get a Random Thing To Do If You're Bored """
        try:
            json = Fun.urljson(
                'https://www.boredapi.com/api/activity', None)
            if json['link'] == "":
                await embed.embedText(ctx, json['type'], json['activity'])
                return
            else:
                await embed.embedText(ctx, json['type'], json['activity']+"\n"+json['link'])
                return
        except Exception as e:
            await ctx.send("An Error Occured")
            return

    @commands.command(aliases=['kanye', 'kw', 'kanyequote'])
    async def kanyewest(self, ctx):
        """ Get a Kanye West Quote """
        async with ctx.message.channel.typing():
            for x in range(0, 5):
                json = Fun.urljson('https://api.kanye.rest/?format=json', None)
                textLower = json['quote'].lower()
                if not any(map(textLower.__contains__, lists.profanity)):
                    await embed.embedText(ctx, json['quote'])
                    return
            await embed.embedText(ctx, 'Could not find a PG Kanye West Quote')
            return

    @commands.command(aliases=['fox'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def foxy(self, ctx):
        """ Get an image of a foxy """
        try:
            json = Fun.urljson('https://randomfox.ca/floof/', None)
            await embed.embedImage(ctx, json['image'])
            return
        except Exception as e:
            await ctx.send("An Error Occured")
            return

    @commands.command(aliases=['dog'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def woof(self, ctx):
        """ Get an image of a Woof """
        try:
            json = Fun.urljson('https://dog.ceo/api/breeds/image/random', None)
            await embed.embedImage(ctx, json['message'])
            return
        except Exception as e:
            await ctx.send("An Error Occured")
            return

    @commands.command(aliases=['cat'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def meow(self, ctx):
        '''Get an image of a Meow'''
        try:
            if self.config.theCatAPI is None or self.config.theCatAPI == "https://thecatapi.com/":
                raise commands.CommandError('TheCatAPI is not setup.')
            json = Fun.urljson('https://api.thecatapi.com/v1/images/search',
                               {'x-api-key': self.config.theCatAPI})

            await embed.embedImage(ctx, (json[0])['url'])
            return
        except Exception as e:
            await ctx.send("An Error Occured")
            return


def setup(bot):
    bot.add_cog(Fun(bot))
