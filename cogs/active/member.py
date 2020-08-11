import os
import discord
from discord.ext import commands

from utils import default


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel

        if channel is not None:
            if str(self.config.welcome).__contains__('member.mention'):
                await channel.send(str(self.config.welcome).replace('member.mention', str(member.mention)))
            else:
                await channel.send(self.config.welcome)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel

        if channel is not None:
            if str(self.config.welcome).__contains__('member.mention'):
                await channel.send(str(self.config.leave).replace('member.mention', str(member.mention)))
            else:
                await channel.send(self.config.leave)

def setup(bot):
    bot.add_cog(Member(bot))
