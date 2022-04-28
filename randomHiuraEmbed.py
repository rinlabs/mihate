import discord
import os
import random
from art import *

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
