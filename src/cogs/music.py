import discord
from discord.ext import commands
from discord.ext.commands import Cog, command

class Music (Cog):
  def __init__(self, bot):
    self.voice_channel = None
    self.bot = bot

  async def in_voice_channel(self):
    if self.voice_channel == None:
      return False
    else:
      return True

  @command()
  async def join(self, ctx):
    author = ctx.message.author
    self.voice_channel = author.voice.channel
    client = await self.voice_channel.connect()    

  @command()
  async def leave(self, ctx):
    if await self.in_voice_channel():
      await ctx.voice_client.disconnect()
      self.voice_channel = None
      return True
    else:
      return False

