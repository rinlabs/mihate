import discord
from modules.aegis.aegis import *
from os.path import join

class aegisEmbed:
    def __init__(self,aegis,message):
        self.aegis = aegis
        self.message = message

    def getFlag(self):
        flagHaus = ""
        flagHyper = ""
        if(len(self.aegis.URLHaus) != 0):
            flagHaus = "\n\nURLHaus Malicious URL Database"
        if(len(self.aegis.hyperphish) != 0):
            flagHyper = "\nHyperphish Phishing URL Database"
        return flagHaus + flagHyper

    def makeDescription(self):
        descHaus = []
        descHyper = []
        descHausStr = ""
        descHyperStr = ""
        for index,i in enumerate(self.aegis.URLHaus):
            if (self.aegis.URLHaus[index].detection != 0):
                    descHaus.append("\n\nURL: "+self.aegis.URLHaus[index].url+"\nThreat: " + self.aegis.URLHaus[index].threat)
        for index,i in enumerate(self.aegis.hyperphish):
            if (self.aegis.hyperphish[index].detection != 0):
                    descHyper.append("\n\nURL: "+self.aegis.hyperphish[index].url+"\nThreat: Phishing Link")

        descHaus = "".join(descHaus)
        descHyper = "".join(descHyper)
        return descHaus + descHyper

    def createEmbed(self):
        embed = discord.Embed(title = "Mihate Hiura",\
                                description="**This link(s) has been flagged by:"+self.getFlag()+self.makeDescription()+"\n\n"\
                                "User "+self.message.author.mention+" tried to send malicious links flagged by one or multiple databases and antivirus engines.**"+"\n\n"+"@here do **NOT** click on these link(s).",\
                                color=0xFF0000)
        return embed
