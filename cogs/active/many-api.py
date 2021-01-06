import os
import discord
from discord.ext import commands

import psutil
import aiohttp
import asyncio
import requests
import time

from utils import default, lists, embed, jsondata


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
        json = ManyAPI.urljson(
            'https://many-api.vercel.app/atla-quote/random', None)
        await embed.embedText(ctx, json['author'], json['quote'])
        return

    @commands.command(aliases=['mcu', 'mcuquote'])
    async def MarvelQuotes(self, ctx):
        """ Get a Random Marvel Quote """
        json = ManyAPI.urljson(
            'https://many-api.vercel.app/marvel-quote/random', None)
        await embed.embedText(ctx, json['author'], json['quote'] + "\n - " + json['movie'])
        return

    @commands.command(aliases=['garfield'])
    async def Garfield(self, ctx):
        """ Get a Random Garfield Comic Strip """
        json = ManyAPI.urljson(
            'https://many-api.vercel.app/garfield/random', None)
        await embed.embedImage(ctx, json['url'])
        return

    @commands.command()
    async def joke(self, ctx):
        """ Get a Random Joke """
        json = ManyAPI.urljson(
            'https://many-api.vercel.app/jokes/random', None)
        await embed.embedText(ctx, json['joke'])
        return

    @commands.command(aliases=['covid'])
    async def covidiso(self, ctx, *, iso: commands.clean_content):
        """ Get The Coronavirus Statistics By ISO """
        try:
            json = (ManyAPI.urljson(
                f'https://many-api.vercel.app/coronavirus/getData?iso={iso.strip()}', None))[0]
            embedColour = discord.Embed.Empty
            embedColour = ctx.me.top_role.colour
            embed = discord.Embed(colour=embedColour)
            embed.set_author(name="Requested by {}".format(
                ctx.message.author.name))
            embed.set_image(
                url=f'https://many-api.vercel.app/coronavirus/getImage?iso={iso.strip()}&type=newCases')
            embed.add_field(name='Date', value=json['date'])
            embed.add_field(name='Total Cases', value=json['total_cases'])
            embed.add_field(name='Total Deaths', value=json['total_deaths'])
            embed.add_field(name='Total Cases Per Million',
                            value=json['total_cases_per_million'])
            embed.add_field(name='Total Deaths Per Million',
                            value=json['total_deaths_per_million'])
            embed.add_field(name='New Cases', value=json['new_cases'])
            embed.add_field(name='New Deaths', value=json['new_deaths'])
            embed.add_field(name='New Cases Per Million',
                            value=json['new_cases_per_million'])
            embed.add_field(name='New Deaths Per Million',
                            value=json['new_deaths_per_million'])
            embed.set_footer(text="Developed by {}".format(
                jsondata.getDeveloper()))
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send('Sorry, an error occured. Please try again later')
        return

    @commands.command(aliases=['isocode'])
    async def iso(self, ctx):
        """ Get ISO Codes For The Coronavirus Statistics """
        try:
            json = (ManyAPI.urljson(
                'https://many-api.vercel.app/coronavirus/getISO', None))
            print(json)

            embedColour = discord.Embed.Empty
            embedColour = ctx.me.top_role.colour
            embed = discord.Embed(colour=embedColour)
            embed.set_author(name="Requested by {}".format(
                ctx.message.author.name))
            indexer = 0
            for x in json.get('iso_code'):
                if indexer > 24:
                    embed.set_footer(text="Developed by {}".format(
                        jsondata.getDeveloper()))
                    await ctx.send(embed=embed)
                    embedColour = discord.Embed.Empty
                    embedColour = ctx.me.top_role.colour
                    embed = discord.Embed(colour=embedColour)
                    embed.set_author(name="Requested by {}".format(
                        ctx.message.author.name))
                    indexer = 0
                embed.add_field(
                    name=x['iso'], value=x['location'], inline=True)
                indexer += 1
            embed.set_footer(text="Developed by {}".format(
                jsondata.getDeveloper()))
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send('Sorry, an error occured. Please try again later')
        return


def setup(bot):
    bot.add_cog(ManyAPI(bot))
