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
    await ctx.send("hi evan")

  @command(name = "help")
  async def help(self, ctx):
      await ctx.send("Muffinwoman Help Page\n---\n.help: This help info.\n.play [url]: Play media from URL and join voice.\n.leave: Stop playing and leave voice channel.\n.join: Force the bot to join your channel.\n.skip: Skip current song.\n.queue: See the current playlist!\n.clearqueue: Reset queue!\n.info: Show software, developer, and license info.\n---\nTip: there is a queue! Just run the .play command to add to it.")

  @command(name = "info")
  async def info(self, ctx):
      await ctx.send("Muffinwoman is created by Cole Vohs. Read the code, create issues, and send patches at the repository: https://github.com/ColeW-Picaro/muffinwoman. Licensed under the GPLv3.")
