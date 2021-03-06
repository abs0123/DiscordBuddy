# bot.py
import os

import json
import discord
import random
import random
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse, re

from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = 'INSERT_TOKEN'
GUILD = 'Nerds'

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'user has connected to Discord!')    
  
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

@bot.command(pass_context=True)
async def randomfact(ctx):
    content = urllib.request.urlopen(
        'https://uselessfacts.jsph.pl/random.json?language=en'
    )
    jsonobj = json.loads(content.read().decode())
    await ctx.send(jsonobj['text'])

@bot.command(pass_context=True)
async def meme(ctx, *, search):
    await ctx.send(bing_image_search(search.split(' ')))


def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

def bing_image_search(search):
    query = '%20'
    query = query.join(search)
    url="http://www.bing.com/images/search?q=" + query + "%20meme&FORM=HDRSC2"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    ActualImages=[] # contains the link for Large original images
    for a in soup.find_all("a",{"class":"iusc"}):
        m = json.loads(a["m"])
        murl = m["murl"] # mobile image
        turl = m["turl"] # desktop image
        ActualImages.append(turl)
    
    return ActualImages[random.randint(0, len(ActualImages) - 10)]
     
bot.run(TOKEN)
