import discord
import os
import random
from art import *
from ownershipDbCon import *

class randomHiuraEmbed:
    def __init__(self,rarity,ctx):
        self.rarity = rarity
        self.semipath = './assets/'+self.rarity+'/'
        self.list = os.listdir(self.semipath)
        self.RNG = random.choice(self.list)
        self.path = self.semipath+self.RNG
        self.userID = ctx.author.id
        self.handle = ctx.author.mention

    def colorGet(self):
        if (self.rarity == 'Common'):
            return 0xffffff
        elif(self.rarity == 'Rare'):
            return 0xa7a7ff
        elif(self.rarity == 'Elite'):
            return 0xff6600
        elif(self.rarity == 'SSR'):
            return 0xfff169
        elif(self.rarity == 'UR'):
            return 0x80ff69

    def setDesc(self):
        if (self.rarity == 'Common'):
            return 'Hmmm, '
        elif(self.rarity == 'Rare'):
            return 'Huh, '
        elif(self.rarity == 'Elite'):
            return 'Damn, '
        elif(self.rarity == 'SSR'):
            return 'Wow! '
        elif(self.rarity == 'UR'):
            return 'Holy Smokes! '

    def makeOwnershipMsg(self):
        if (getOwnership(self.userID,self.RNG,self.rarity) == 0):
            return 'Neat! You have found a new variant of Hiura!'
        else:
            return ""

    def createFile(self):
        return discord.File(self.path,filename = "image.jpg")

    def createEmbed(self):
        embed = discord.Embed(title = "Mihate Hiura",\
                                description=self.setDesc()+self.handle+" rolled a "+self.rarity+" Hiura!"+"\n\n"+self.makeOwnershipMsg(),\
                                color=self.colorGet())
        attach =  self.createFile()
        embed.set_image(url='attachment://image.jpg')
        return embed
