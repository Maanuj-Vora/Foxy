import discord
from discord.ext import commands


async def embedImage(ctx, img_url):
    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour
    embed = discord.Embed(colour=embedColour)
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)


async def embedText(ctx, title, value):
    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour
    embed = discord.Embed(colour=embedColour)
    if(title == ""):
        embed.add_field(name='\u200b', value=value)
    else:
        embed.add_field(name=title, value=value)
    await ctx.send(embed=embed)
