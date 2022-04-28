import discord
import logging
import os
from art import *
from random import *
import random
import time
from discord.ext import commands
import requests
import json
from urlextract import URLExtract
from urllib.parse import urlparse

#logging
logging.basicConfig(level=logging.INFO)
#prefix
mihate = commands.Bot(command_prefix=(os.environ['PREFIX']))
#token
mihate.run(os.environ['TOKEN'])

#token = input("Enter bot token: ")

#aegis
linksJSON = json.loads(requests.get("https://api.hyperphish.com/gimme-domains").text)

class randomHiuraEmbed:
    def __init__(self,rarity):
        self.rarity = rarity
        self.semipath = './assets/'+self.rarity+'/'
        self.list = os.listdir(self.semipath)
        self.RNG = random.choice(self.list)
        self.path = self.semipath+self.RNG;

    def colorGet(self):
        if (self.rarity == 'Common'):
            return 0xffffff
        elif(self.rarity == 'Rare'):
            return 0xa7a7ff
        elif(self.rarity == 'Elite'):
            return 0xcda7ff
        elif(self.rarity == 'SSR'):
            return 0xfff169
        elif(self.rarity == 'UR'):
            return 0x80ff69

    def createFile(self):
        return discord.File(self.path,filename = "image.jpg")

    def createEmbed(self):
        embed = discord.Embed(title = "Mihate Hiura",description="You rolled a "+self.rarity+" Hiura! "+randart(),color=self.colorGet())
        attach =  self.createFile()
        embed.set_image(url='attachment://image.jpg')
        return embed

# on-ready console notification & bot presence
@mihate.event
async def on_ready():
    os.system("cls")
    print(text2art("mihate", font='tarty1'))
    print("Logged in as {0.user}".format(mihate))
    await mihate.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=(mihate.command_prefix + "help")))

# AEGIS anti spam link protection
@mihate.event
async def on_message(message):

    if message.author == mihate.user:
        return
    if (URLExtract().has_urls(message.content) == True):
        if (urlparse(URLExtract().find_urls(message.content)[0]).netloc in linksJSON):
            print('\033[31m'+text2art("!aegis!", font='tarty1'))
            print('A message containing illegal link '+message.content+' sent by '+message.author.name+'#'+message.author.discriminator+' was detected by AEGIS')
            #await message.delete()
            await message.channel.send(">>> **User "+message.author.mention+" tried to send malicious links.**"+"\n\n"+"@here do **NOT** click on these link(s)."+"\n\n"+"These link(s) will steal your account information at best and compromise your machine at worst.")
        await mihate.process_commands(message)
    elif (URLExtract().has_urls(message.content) == False):
        await mihate.process_commands(message)

# greet command
@mihate.command(help="Greets the user")
async def greet(ctx):
    await ctx.channel.send("Hello, I'm Mihate Hiura!")
    await ctx.channel.send(
        "https://cloud.neoservices.xyz/f/97138729272743b595af/?raw=1")

# change prefix command
@mihate.command(help="Change the prefix of the bot")
async def prefix(ctx, prefArg):
    dispNP = "The new bot prefix is " + prefArg
    await ctx.channel.send(dispNP)
    mihate.command_prefix = prefArg
    await mihate.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=(mihate.command_prefix + "help")))

# random lineart command
@mihate.command(help="Sends a random ASCII line art")
async def lineart(ctx):
    await ctx.channel.send(randart())

# random hiura image
@mihate.command(help="Sends an image of Hiura with randomized rarity")
async def imageroll(ctx):
    seed(round(time.time() * 1000))
    rng = randint(0,1000)
    name = "Mihate Hiura"
    if(0<rng<450):
            commonHiura = randomHiuraEmbed('Common')
            await ctx.channel.send(file=commonHiura.createFile(),embed=commonHiura.createEmbed())
    elif(450<rng<750):
            rareHiura = randomHiuraEmbed('Rare')
            await ctx.channel.send(file=rareHiura.createFile(),embed=rareHiura.createEmbed())
    elif(750<rng<850):
            eliteHiura = randomHiuraEmbed('Elite')
            await ctx.channel.send(file=eliteHiura.createFile(),embed=eliteHiura.createEmbed())
    elif(850<rng<975):
            ssrHiura = randomHiuraEmbed('SSR')
            await ctx.channel.send(file=ssrHiura.createFile(),embed=ssrHiura.createEmbed())
    elif(975<rng<1000):
            urHiura = randomHiuraEmbed('UR')
            await ctx.channel.send(file=urHiura.createFile(),embed=urHiura.createEmbed())
