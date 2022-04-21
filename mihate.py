import discord
import logging
import os
from random import seed
from random import randint

logging.basicConfig(level=logging.INFO)

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send("Hello! I'm Mihate")
        await message.channel.send("https://i0.wp.com/wibumesta.com/wp-content/uploads/2021/07/3306977_791_1084_173752.jpeg?resize=791%2C1084&ssl=1")

client.run(os.environ['TOKEN'])
