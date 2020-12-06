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
    self.playlist = []
    self.now_playing = False
    
  # Helper function to check if bot is in a voice channel
  async def in_voice_channel(self):
    if self.voice_channel == None:
      return False
    else:
      return True

  # Command to join the channel the user is in
  @command()
  async def join(self, ctx):
    author = ctx.message.author
    self.voice_channel = author.voice.channel
    client = await self.voice_channel.connect()    

  # Command to leave the channel the user is in
  @command()
  async def leave(self, ctx):
    if await self.in_voice_channel():
      await ctx.voice_client.disconnect()
      self.voice_channel = None
      return True
    else:
      return False

  # Plays a song on a voice channel
  def play_song(self, botvoice, song):    
    source = discord.FFmpegPCMAudio(song.stream_url)
    
    def after_playing(err):
      if len(self.playlist) > 0:
        next_song = self.playlist.pop(0)        
        self.play_song(botvoice, next_song)
      else:
        self.now_playing = False
        return
      
    self.now_playing = True
    botvoice.play(source, after=after_playing)    

  # Command that takes a url to play a song
  @command()
  async def play (self, ctx, url):
    if self.voice_channel == None:
      await self.join (ctx)
    
    author = ctx.message.author    
    video = Video(url, author)
    botvoice = ctx.voice_client    
    self.playlist.append(video) 
    if self.now_playing:
      await ctx.send("added to queue: " + video.title)
      return
    else:      
      await ctx.send("now playing: " + video.title)
      self.play_song(botvoice, self.playlist.pop(0))

  @command()
  async def skip (self, ctx):
    botvoice = ctx.voice_client
    botvoice.stop()
    if len(self.playlist) > 0:
        next_song = self.playlist.pop(0)
        self.play_song(botvoice, next_song)
        await ctx.send("Playing: " + next_song.title)
    else:
        self.now_playing = False
        await ctx.send("Playlist empty!")
        return

  @command()
  async def pause (self, ctx):
    botvoice = ctx.voice_client
    botvoice.pause()
    await ctx.send("Music paused!")

  @command()
  async def resume (self, ctx):
    botvoice = ctx.voice_client
    botvoice.resume()
    await ctx.send("Music resumed!")

  @command()
  async def queue (self, ctx):
    if self.playlist == []:
        await ctx.send("Playlist empty!")
        return
    else:
        message = "Current playlist:\n"
        stringlist = []
        for video in self.playlist:
            stringlist.append(video.title)
        message += "\n".join(stringlist)
        await ctx.send(message)

  @command()
  async def clearqueue (self, ctx):
      if self.playlist == []:
          await ctx.send("Playlist is empty!")
          return
      else:
          self.playlist = []
          await ctx.send("Playlist has been cleared!")
          return
