import asyncio
from datetime import date, datetime

import psutil
import os
import time
import aiohttp
import discord
from discord.ext import commands
from utils import default, embed
import requests


QUERY_EXCEPTIONS = None
QUERY_ERROR = None


class Animal(commands.Cog):
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
    bot.add_cog(Animal(bot))
