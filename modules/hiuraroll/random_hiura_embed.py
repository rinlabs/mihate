import os
import sys
import random
import discord
from modules.db.ownership_db_con import get_ownership

# class constructor
class RandomHiuraEmbed:
    """Creates hiuraroll embed"""
    def __init__(self, rarity, ctx):
        self.rarity = rarity
        self.semipath = './assets/embeds/hiuraroll/'+self.rarity+'/'
        # lists all picture in a directory
        self.list = os.listdir(self.semipath)
        # randomly pick an image
        self.rng = random.choice(self.list)
        # sets the image path
        self.path = self.semipath+self.rng
        # command issuer's userid
        self.user_id = ctx.author.id
        # command issuer's discord handle
        self.handle = ctx.author.mention

    # returns border color based on the rarity
    def color_get(self):
        """Returns hiuraroll color for specific rarity"""
        if  self.rarity == 'Common' :
            return 0xffffff
        elif self.rarity == 'Rare' :
            return 0xa7a7ff
        elif self.rarity == 'Elite' :
            return 0xff6600
        elif self.rarity == 'SSR' :
            return 0xfff169
        elif self.rarity == 'UR' :
            return 0x80ff69

    # returns description based on the rarity
    def set_desc(self):
        """Returns hiuraroll description for specific rarity"""
        if  self.rarity == 'Common' :
            return 'Hmmm, '
        elif self.rarity == 'Rare' :
            return 'Huh, '
        elif self.rarity == 'Elite' :
            return 'Damn, '
        elif self.rarity == 'SSR' :
            return 'Wow! '
        elif self.rarity == 'UR' :
            return 'Holy Smokes! '

    # set additional message based on ownership
    def make_ownership_msg(self):
        """Returns hiuraroll ownership status"""
        if get_ownership(self.user_id, self.rng, self.rarity) == 0:
            return 'Neat! You have found a new variant of Hiura!'
        else:
            return ""

    # creates embed picture
    def create_file(self):
        """Returns hiuraroll embed thumbnail"""
        return discord.File(self.path, filename="image.jpg")

    # creates embed
    def create_embed(self):
        """Returns hiuraroll embed"""
        embed = discord.Embed(description=self.set_desc()+self.handle+" rolled a "+self.rarity
                              + " Hiura!"+"\n\n"+self.make_ownership_msg(),
                              color=self.color_get())
        embed.set_author(name="Mihate Hiura")
        embed.set_footer(text="© Rinlabs 2022")
        embed.set_image(url='attachment://image.jpg')
        return embed
