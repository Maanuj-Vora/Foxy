import os
import discord
from discord.ext import commands

from utils import default
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    async def news(self, ctx, *, number):
        """ Gets The Top News Articles From Google News """
        try:
            numMax = int(number)
            if(numMax > 10):
                numMax = 10
            elif(numMax < 1):
                numMax = 1
        except Exception as e:
            numMax = 5

        xml_page = urlopen('https://news.google.com/news/rss').read()
        news_list = soup(xml_page, "xml").findAll("item")

        embedColour = discord.Embed.Empty
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour
        embed = discord.Embed(colour=embedColour)

        x = 0
        for news in news_list:
            if(x < numMax):
                embed.add_field(name=f"{x+1}) {news.title.text}",
                                value=f"{news.link.text}\n{news.pubDate.text}", inline=False)
                x = x+1

        await ctx.send(content=f"Top {numMax} news from Google News.\nRequested by {ctx.message.author.mention}", embed=embed)


def setup(bot):
    bot.add_cog(News(bot))
