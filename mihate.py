import discord
import logging
import os
from random import seed
from random import randint

logging.basicConfig(level=logging.INFO)

client = discord.Client()

prefix = "%"
#prefix = (os.environ['PREFIX'])
token = input("Enter bot token: ")


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="%help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix + "help"):
        await message.channel.send("**Mihate** Commands: \n")
        await message.channel.send("\n`" + prefix + "greet` - greets the user")
    elif message.content.startswith(prefix + "greet"):
        await message.channel.send("Hello, I'm Mihate Hiura!")
        await message.channel.send("https://cloud.neoservices.xyz/f/97138729272743b595af/?raw=1")

# dev token
client.run(token)
# client.run(os.environ['TOKEN'])
