# bot.py
import os

import discord
import random
import urllib.parse, urllib.request, re

from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'INSERT_TOKEN_HERE'
GUILD = 'Nerds'

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'user has connected to Discord!')

#@bot.event
#async def on_message(message):
#    if ("memebot" or "MemeBot" or "MemeBot" in message.content) and ("Hi, I'm Memebot and I think you have a large pee-pee! UwU" not in message.content):
#        await message.channel.send("Hi, I'm Memebot and I think you have a large pee-pee! UwU")
    
  
@bot.command(pass_context=True)
async def youtube(ctx, *, search):
    query = urllib.parse.urlencode({
        'search_query': search
    })
    content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query
    )
    search_results = re.findall('/watch\?v=(.{11})', content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + random.choice(search_results[0:5]))
     
bot.run(TOKEN)


