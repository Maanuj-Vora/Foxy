import discord
from discord.ext import commands
from multipledispatch import dispatch
import requests

from utils import jsondata

async def embedImage(ctx, img_url):
    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour
    embed = discord.Embed(colour=embedColour)
    embed.set_image(url=img_url)
    embed.set_author(name="Requested by {}".format(ctx.message.author.name))
    embed.set_footer(text="Developed by {}".format(jsondata.getDeveloper()))
    await ctx.send(embed=embed)
    return

@dispatch(object, str, str)
async def embedText(ctx, title, value):
    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour
    embed = discord.Embed(colour=embedColour)
    embed.add_field(name=title, value=value)
    embed.set_author(name="Requested by {}".format(ctx.message.author.name))
    embed.set_footer(text="Developed by {}".format(jsondata.getDeveloper()))
    await ctx.send(embed=embed)

@dispatch(object, str)
async def embedText(ctx, value):
    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour
    embed = discord.Embed(colour=embedColour)
    embed.add_field(name='\u200b', value=value+'\n\u200b')
    embed.set_author(name="Requested by {}".format(ctx.message.author.name))
    embed.set_footer(text="Developed by {}".format(jsondata.getDeveloper()))
    await ctx.send(embed=embed)
    return


# async def embedText(ctx, title, value):
#     embedColour = discord.Embed.Empty
#     if hasattr(ctx, 'guild') and ctx.guild is not None:
#         embedColour = ctx.me.top_role.colour
#     embed = discord.Embed(colour=embedColour)
#     if(title == ""):
#         embed.add_field(name='\u200b', value=value+'\n\u200b')
#     else:
#         embed.add_field(name=title, value=value)
#     embed.set_author(name="Requested by {}".format(ctx.message.author.name))
#     embed.set_footer(text="Developed by {}".format("Rainbwshep#4828"))
#     await ctx.send(embed=embed)
