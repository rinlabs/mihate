import discord
import logging
from dotenv import load_dotenv
import os
from art import *
from random import *
import random
import time
from discord.ext import commands
import requests
import json
from modules.cli.clearScreen import *
from modules.hiuraroll.randomHiuraEmbed import *
from modules.db.ownershipDbCon import *
from modules.aegis.aegisEmbed import *

#load_dotenv
load_dotenv('.env')
#logging
logging.basicConfig(level=logging.INFO)
#prefix
mihate = commands.Bot(command_prefix=os.getenv('PREFIX'),activity=discord.Activity(type=discord.ActivityType.listening,name=(os.getenv('PREFIX') + "help")))

# on-ready console notification & bot presence
@mihate.event
async def on_ready():
    clear()
    print(text2art("mihate", font='tarty1'))
    print("Logged in as {0.user}".format(mihate))

# AEGIS anti spam link protection
@mihate.event
async def on_message(message):
    # checks if the author is the bot itself
    if message.author == mihate.user:
        return
    else:
        if (URLExtract().has_urls(urlCheck(message.content)) == True):
            aAnalysis = aegis(message.content)
            if (aAnalysis.threatValue !=0):
                aEmbed = aegisEmbed(aAnalysis,message)
                await message.channel.send(embed=aEmbed.createEmbed())
                await mihate.process_commands(message)
        await mihate.process_commands(message)

# greet command
@mihate.command(help="Greets the user")
async def greet(ctx):
    await ctx.channel.send("Hello, I'm Mihate Hiura!")
    await ctx.channel.send(
        "https://cloud.neoservices.xyz/f/97138729272743b595af/?raw=1")

# random lineart command
@mihate.command(help="Sends a random ASCII line art")
async def lineart(ctx):
    await ctx.channel.send(randart())

# random hiura image
@mihate.command(help="Sends an image of Hiura with randomized rarity")
async def hiuraroll(ctx):
    # sets random seed number based on system time
    seed(round(time.time() * 1000))
    rng = randint(0,1000)

    name = "Mihate Hiura"
    if(0<rng<550):
            commonHiura = randomHiuraEmbed('Common',ctx)
            await ctx.channel.send(file=commonHiura.createFile(),embed=commonHiura.createEmbed())
            makeOwnership(commonHiura.userID,commonHiura.RNG,'Common')
    elif(550<rng<750):
            rareHiura = randomHiuraEmbed('Rare',ctx)
            await ctx.channel.send(file=rareHiura.createFile(),embed=rareHiura.createEmbed())
            makeOwnership(rareHiura.userID,rareHiura.RNG,'Rare')
    elif(750<rng<850):
            eliteHiura = randomHiuraEmbed('Elite',ctx)
            await ctx.channel.send(file=eliteHiura.createFile(),embed=eliteHiura.createEmbed())
            makeOwnership(eliteHiura.userID,eliteHiura.RNG,'Elite')
    elif(850<rng<975):
            ssrHiura = randomHiuraEmbed('SSR',ctx)
            await ctx.channel.send(file=ssrHiura.createFile(),embed=ssrHiura.createEmbed())
            makeOwnership(ssrHiura.userID,ssrHiura.RNG,'SSR')
    elif(975<rng<1000):
            urHiura = randomHiuraEmbed('UR',ctx)
            await ctx.channel.send(file=urHiura.createFile(),embed=urHiura.createEmbed())
            makeOwnership(urHiura.userID,urHiura.RNG,'UR')
mihate.run(os.getenv('TOKEN'))
