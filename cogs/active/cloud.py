import os
import discord
from discord.ext import commands

import psutil
import aiohttp
import asyncio

from utils import default, mongo


class Cloud(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command(aliases=['tme'])
    async def toggleMemberEntry(self, ctx):
        """ Toggle Member Entry Message On/Off """
        await ctx.send(mongo.toggleMemberEntry(ctx.message.guild))

    @commands.command(aliases=['cmem'])
    async def changeMemberEntryMessage(self, ctx, *, message: commands.clean_content):
        """ Changes Content of Member Entry Message """
        updatedMessage = mongo.changeMemberEntryMessage(
            ctx.message.guild, message)
        if updatedMessage.__contains__('member.mention'):
            updatedMessage = updatedMessage.replace(
                'member.mention', str(ctx.message.author.mention))
        await ctx.send(updatedMessage)

    @ commands.command(aliases=['tml'])
    async def toggleMemberLeave(self, ctx):
        """ Toggle Member Leave Message On/Off """
        await ctx.send(mongo.toggleMemberLeave(ctx.message.guild))

    @commands.command(aliases=['cmlm'])
    async def changeMemberLeaveMessage(self, ctx, *, message: commands.clean_content):
        """ Changes Content of Member Leave Message """
        updatedMessage = mongo.changeMemberLeaveMessage(
            ctx.message.guild, message)
        if updatedMessage.__contains__('member.mention'):
            updatedMessage = updatedMessage.replace(
                'member.mention', str(ctx.message.author.mention))
        await ctx.send(updatedMessage)


def setup(bot):
    bot.add_cog(Cloud(bot))
