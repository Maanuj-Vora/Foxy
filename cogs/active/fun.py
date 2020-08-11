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
        self.QUERY_EXCEPTIONS = (
            discord.HTTPException, aiohttp.ClientError, asyncio.TimeoutError, commands.CommandError)
        self.QUERY_ERROR = commands.CommandError(
            'Query failed. Try again later.')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult the supreme, all knowing 8ball to receive an answer """
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {random.choice(lists.ballresponse)}")

    @commands.command(aliases=['cn', 'cnjoke'])
    async def chucknorris(self, ctx):
        """ Get a Chuck Norris Joke """
        try:
            response = requests.get('http://api.icndb.com/jokes/random')
            if response.status_code != 200:
                raise QUERY_ERROR
            json = response.json()
            text = json['value'].get('joke')
            await embed.embedText(ctx, 'Chuck Norris', text)
        except self.QUERY_EXCEPTIONS:
            raise QUERY_ERROR

    @commands.command(aliases=['fox'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def foxy(self, ctx):
        """ Get an image of a foxy """

        try:
            response = requests.get('https://randomfox.ca/floof/')
            if response.status_code != 200:
                raise QUERY_ERROR
            json = response.json()
            img_url = json['image']
            await embed.embedImage(ctx, img_url)
        except self.QUERY_EXCEPTIONS:
            raise QUERY_ERROR

    @commands.command(aliases=['dog'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def woof(self, ctx):
        """ Get an image of a Woof """

        try:
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            if response.status_code != 200:
                raise QUERY_ERROR
            json = response.json()
            img_url = json['message']
            await embed.embedImage(ctx, img_url)
        except self.QUERY_EXCEPTIONS:
            raise QUERY_ERROR

    @commands.command(aliases=['cat'])
    @commands.cooldown(rate=6, per=10.0, type=commands.BucketType.user)
    @commands.bot_has_permissions(embed_links=True)
    async def meow(self, ctx):
        '''Get an image of a Meow'''

        if self.config.theCatAPI is None or self.config.theCatAPI == "https://thecatapi.com/":
            raise commands.CommandError('TheCatAPI is not setup.')
        try:
            resp = requests.get('https://api.thecatapi.com/v1/images/search',
                                headers={'x-api-key': self.config.theCatAPI})
            if resp.status_code != 200:
                raise QUERY_ERROR
            json = resp.json()
            data = json[0]
            img_url = data['url']
            await embed.embedImage(ctx, img_url)
        except self.QUERY_EXCEPTIONS:
            raise QUERY_ERROR



def setup(bot):
    bot.add_cog(Fun(bot))
