import os
import discord
from discord.ext import commands

import psutil
import aiohttp
import asyncio
import requests
import time

from utils import default, lists, embed


class ManyAPI(commands.Cog):
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


    @commands.command(aliases=['atla', 'avatarquote'])
    async def ATLAQuotes(self, ctx):
        """ Get a Random ATLA Quote """
        async with ctx.message.channel.typing():
            json = ManyAPI.urljson('https://many-api.vercel.app/atla-quote/random', None)
            await embed.embedText(ctx, json['author'], json['quote'])
            return


def setup(bot):
    bot.add_cog(ManyAPI(bot))
