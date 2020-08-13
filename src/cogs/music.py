# Filename: meta.py
# Author: Cole Vohs
# Description: Music related commands for the bot

import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from video import Video

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

  # Play a song at url
  @command()
  async def play (self, ctx, url):
    if self.voice_channel == None:
      await self.join (ctx)
    else:
      return
    author = ctx.message.author    
    video = Video(url, author)
    botvoice = ctx.voice_client
    source = discord.FFmpegPCMAudio(video.stream_url)
    botvoice.play (source)


