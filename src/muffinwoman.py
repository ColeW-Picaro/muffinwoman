# Filename: muffinwoman.py
# Author: Cole Vohs
# Description: Creates a discord bot, initializes commands, and runs it

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot, command
from cogs.meta import Meta
from cogs.music import Music

class Muffinwoman ():

  def __init__(self):
    # Create Bot and add the cogs
    self.bot = Bot(command_prefix = '.', help_command = None, description = None)
    self.bot.add_cog(Meta(self.bot))
    self.bot.add_cog(Music(self.bot))

    # fetch the token from the environment variable
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    # run the bot
    self.bot.run(token)
