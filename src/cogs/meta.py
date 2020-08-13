# Filename: meta.py
# Author: Cole Vohs
# Description: Meta commands for the bot

import discord
from discord.ext import commands
from discord.ext.commands import Cog, command

class Meta (Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name = "sendhelp")
  async def sendhelp(self, ctx):
    await ctx.send("https://media1.tenor.com/images/a4ac5e98359e8b47f47425a1fb4a566f/tenor.gif?itemid=4941905")

  @command(name = "ses")
  async def ses(self, ctx):
    await ctx.send("fuck you evan")