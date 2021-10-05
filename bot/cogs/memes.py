import discord
from discord.ext import commands
import random
import aiohttp

class memecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def givetea(self,ctx):
        member = ctx.author
        role = discord.utils.get(member.guild.roles, name="Tea")
        if role in member.roles:
            await ctx.send(ctx.author.mention+" , you already have this role. XD")
        else:
            await member.add_roles(role)
            await ctx.send("Great!"+ ctx.author.mention + " has access to "+self.bot.get_channel(891731713326202890).mention)
    

def setup(bot):
    bot.add_cog(memecog(bot))