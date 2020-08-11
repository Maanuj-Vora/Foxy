import os
import discord
from discord.ext import commands

from utils import default

import requests
import json


class UrlShort(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=['shorten', 'urlshorten'])
    async def urlshort(self, ctx, *, url):
        """ Shortens a URL """

        url = "http://google.com".strip()
        data = {'url': url}
        req = requests.post('https://rel.ink/api/links/', data=data).text
        jsonUrl = json.loads(req)
        hashid = jsonUrl.get('hashid')

        await ctx.send(f'{ctx.message.author.mention} Your shortened url is\nhttps://rel.ink/{hashid}')


def setup(bot):
    bot.add_cog(UrlShort(bot))
