import os
import discord
from discord.ext import commands

from utils import default, embed

import requests
import json


class UrlStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=['shorten', 'urlshorten'])
    async def urlshort(self, ctx, *, url):
        """ Shortens a URL """

        url = url.strip()
        data = {'url': url}
        req = requests.post('https://rel.ink/api/links/', data=data).text
        jsonUrl = json.loads(req)
        hashid = jsonUrl.get('hashid')

        await ctx.send(f'{ctx.message.author.mention} Your shortened url is\nhttps://rel.ink/{hashid}')
        return

    @commands.command(aliases=['ws'])
    async def websitestatus(self, ctx, *, url):
        """ Finds the Status of a Website """

        url = url.strip()
        statusCode = requests.get(url).status_code
        await embed.embedImage(ctx, f"https://http.cat/{str(statusCode)}.jpg")
        return

def setup(bot):
    bot.add_cog(UrlStuff(bot))
