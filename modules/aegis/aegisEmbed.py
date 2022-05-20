import discord
from modules.aegis.aegis import *

class aegisEmbed:
    def __init__(self,aegis,message):
        self.aegis = aegis
        self.message = message

    def makeDescription(self):
        descHaus = ""
        descHyper =""

        if (self.aegis.URLHaus.detection != 0):
                descHaus = "\n\nURLHaus Malicious URL Database\n\nThreat: " + self.aegis.URLHaus.threat + "\nThreat Signature: " + self.aegis.URLHaus.signature
        if (self.aegis.hyperphish != 0):
                descHyper = "\n\nHyperphish Phishing URL Database""\n\nThreat: Phishing Link"

        return descHaus + descHyper

    def createEmbed(self):
        embed = discord.Embed(title = "Mihate Hiura",\
                                description="**This link(s) has been flagged by:"+self.makeDescription()+"\n\n"\
                                "User "+self.message.author.mention+" tried to send malicious links flagged by one or multiple databases and antivirus engines.**"+"\n\n"+"@here do **NOT** click on these link(s).",\
                                color=0xFF0000)
        return embed
