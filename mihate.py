import discord
import logging
import os
from art import *
from random import *
import random

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
    seed(109)
    rng = randint(0,1000)
    if(0<rng<599):
            common = './assets/Common/'
            cList = os.listdir(common)
            cRNG = random.choice(cList)
            cPath = common+cRNG;
            await ctx.channel.send(file=discord.File(cPath))
    elif(600<rng<850):
            common = './assets/Elite/'
            eList = os.listdir(common)
            eRNG = random.choice(cList)
            ePath = common+cRNG;
            await ctx.channel.send(file=discord.File(ePath))
    elif(851<rng<980):
            common = './assets/Rare/'
            rList = os.listdir(common)
            rRNG = random.choice(cList)
            rPath = common+cRNG;
            await ctx.channel.send(file=discord.File(rPath))
    elif(981<rng<998):
            common = './assets/SSR/'
            sList = os.listdir(common)
            sRNG = random.choice(cList)
            sPath = common+cRNG;
            await ctx.channel.send(file=discord.File(sPath))
    elif(999<rng<1000):
            common = './assets/UR/'
            uList = os.listdir(common)
            uRNG = random.choice(cList)
            uPath = common+cRNG;
            await ctx.channel.send(file=discord.File(uPath))

# dev token
client.run(token)
# client.run(os.environ['TOKEN'])
