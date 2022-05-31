import discord
import os
import random
from modules.db.ownershipDbCon import getOwnership


# class constructor
class randomHiuraEmbed:
    def __init__(self, rarity, ctx):
        self.rarity = rarity
        self.semipath = './assets/embeds/hiuraroll/'+self.rarity+'/'
        # lists all picture in a directory
        self.list = os.listdir(self.semipath)
        # randomly pick an image
        self.RNG = random.choice(self.list)
        # sets the image path
        self.path = self.semipath+self.RNG
        # command issuer's userid
        self.userID = ctx.author.id
        # command issuer's discord handle
        self.handle = ctx.author.mention

    # returns border color based on the rarity
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

    # returns description based on the rarity
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

    # set additional message based on ownership
    def makeOwnershipMsg(self):
        if (getOwnership(self.userID, self.RNG, self.rarity) == 0):
            return 'Neat! You have found a new variant of Hiura!'
        else:
            return ""

    # creates embed picture
    def createFile(self):
        return discord.File(self.path, filename="image.jpg")

    # creates embed
    def createEmbed(self):
        embed = discord.Embed(title="Mihate Hiura",
                              description=self.setDesc()+self.handle+" rolled a "+self.rarity
                              + " Hiura!"+"\n\n"+self.makeOwnershipMsg(),
                              color=self.colorGet())
        embed.set_image(url='attachment://image.jpg')
        return embed
