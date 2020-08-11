import asyncio
from datetime import date, datetime

import psutil
import os
import time
import aiohttp
import discord
from discord.ext import commands
from utils import default
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
    @commands.bot_has_permissions(embed_links=True)
    async def foxy(self, ctx):
        """ Get an image of a foxy """

        try:
            response = requests.get('https://randomfox.ca/floof/')
            if response.status_code != 200:
                raise QUERY_ERROR

            json = response.json()

            img_url = json['image']

            embedColour = discord.Embed.Empty
            if hasattr(ctx, 'guild') and ctx.guild is not None:
                embedColour = ctx.me.top_role.colour

            embed = discord.Embed(colour=embedColour)
            embed.set_image(url=img_url)
            await ctx.send(embed=embed)

        except self.QUERY_EXCEPTIONS:
            raise QUERY_ERROR


def setup(bot):
    bot.add_cog(Animal(bot))
