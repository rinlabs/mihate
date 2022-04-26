import discord
import logging
import os
from art import *

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


# dev token
client.run(token)
# client.run(os.environ['TOKEN'])
