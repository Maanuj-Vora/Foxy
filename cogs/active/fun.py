import os
import discord
from discord.ext import commands

import random
import aiohttp
import asyncio
import requests

from utils import default, lists, embed

QUERY_EXCEPTIONS = None
QUERY_ERROR = None


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
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


def setup(bot):
    bot.add_cog(Fun(bot))
