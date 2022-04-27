import discord
import logging
import os
from art import *
from random import *
import random
import time

from discord.ext import commands

logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix="%")

# prefix = (os.environ['PREFIX'])
token = input("Enter bot token: ")

# on-ready console notification & bot presence
@client.event
async def on_ready():
    os.system("cls")
    print(text2art("mihate", font='tarty1'))
    print("Logged in as {0.user}".format(client))
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=(client.command_prefix + "help")))

# greet command
@client.command(help="Greets the user")
async def greet(ctx):
    await ctx.channel.send("Hello, I'm Mihate Hiura!")
    await ctx.channel.send(
        "https://cloud.neoservices.xyz/f/97138729272743b595af/?raw=1")

# change prefix command
@client.command(help="Change the prefix of the bot")
async def prefix(ctx, prefArg):
    dispNP = "The new bot prefix is " + prefArg
    await ctx.channel.send(dispNP)
    client.command_prefix = prefArg
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=(client.command_prefix + "help")))

# random lineart command
@client.command(help="Sends a random ASCII line art")
async def lineart(ctx):
    await ctx.channel.send(randart())

# random hiura image
@client.command(help="Sends an image of Hiura with randomized rarity")
async def imageroll(ctx):
    seed(round(time.time() * 1000))
    rng = randint(0,1000)
    if(0<rng<599):
            cCommon = './assets/Common/'
            cList = os.listdir(cCommon)
            cRNG = random.choice(cList)
            cPath = cCommon+cRNG;
            await ctx.channel.send(file=discord.File(cPath))
    elif(599<rng<850):
            eCommon = './assets/E/'
            eList = os.listdir(eCommon)
            eRNG = random.choice(eList)
            ePath = eCommon+eRNG;
            await ctx.channel.send(file=discord.File(ePath))
    elif(850<rng<980):
            rCommon = './assets/Rare/'
            rList = os.listdir(rCommon)
            rRNG = random.choice(rList)
            rPath = rCommon+rRNG;
            await ctx.channel.send(file=discord.File(rPath))
    elif(980<rng<998):
            sCommon = './assets/SSR/'
            sList = os.listdir(sCommon)
            sRNG = random.choice(sList)
            sPath = sCommon+sRNG;
            await ctx.channel.send(file=discord.File(sPath))
    elif(998<rng<1000):
            uCommon = './assets/UR/'
            uList = os.listdir(uCommon)
            uRNG = random.choice(uList)
            uPath = uCommon+uRNG;
            await ctx.channel.send(file=discord.File(uPath))

# dev token
client.run(token)
# client.run(os.environ['TOKEN'])
