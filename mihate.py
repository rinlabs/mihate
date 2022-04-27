import discord
import logging
import os
from art import *
from random import *
import random
import time
from discord.ext import commands

logging.basicConfig(level=logging.DEBUG)

client = commands.Bot(command_prefix="%")

# prefix = (os.environ['PREFIX'])
token = input("Enter bot token: ")

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

# dev token
client.run(token)
# client.run(os.environ['TOKEN'])
