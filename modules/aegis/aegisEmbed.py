import discord


class aegisEmbed:
    # class constructor
    def __init__(self, aegis, message):
        # aegis class
        self.aegis = aegis
        # command issuer message class
        self.message = message

    def getFlag(self):
        flagHaus = ""
        flagHyper = ""
        flagAIPDB = ""

        # adds URLHaus to flag
        if(len(self.aegis.URLHaus) != 0):
            flagHaus = "\nURLHaus Malicious URL Database"

        # adds Hyperphish to flag
        if(len(self.aegis.hyperphish) != 0):
            flagHyper = "\nHyperphish Phishing URL Database"

        # adds Hyperphish to flag
        if(len(self.aegis.abuseipdb) != 0):
            flagAIPDB = "\nAbuseIPDB IP Reputation Center"

        return flagHaus + flagHyper + flagAIPDB

    def makeDescription(self):
        descHaus = []
        descHyper = []
        descAIPDB = []
        descHausStr = ""
        descHyperStr = ""
        descAIPDBStr = ""

        # adds URL + threat to URLHaus array
        for index, i in enumerate(self.aegis.URLHaus):
            descHaus.append("\n\nURL: "+self.aegis.URLHaus[index].url
                            + "\nThreat: "
                            + self.aegis.URLHaus[index].threat)

        # adds URL + threat to hyperphish array
        for index, i in enumerate(self.aegis.hyperphish):
            descHyper.append("\n\nURL: "+self.aegis.hyperphish[index].url
                             + "\nThreat: Phishing Link")

        # adds URL + details to abuseipdb array
        for index, i in enumerate(self.aegis.abuseipdb):
            descAIPDB.append("\n\nURL: "+self.aegis.abuseipdb[index].domain
                             + "\nIP: "+self.aegis.abuseipdb[index].ip
                             + "\nAbuse Confidence Score: "
                             + str(self.aegis.abuseipdb[index].abuseConfidence)
                             + "\nCountry: "
                             + self.aegis.abuseipdb[index].country
                             + "\nReports: "
                             + str(self.aegis.abuseipdb[index].totalReports)
                             + "\nIP Type: "+self.aegis.abuseipdb[index].ipType)
        # converts array to string
        descHausStr = "".join(descHaus)
        # converts array to string
        descHyperStr = "".join(descHyper)
        descAIPDBStr = "".join(descAIPDB)
        return descHausStr + descHyperStr + descAIPDBStr

    # creates embed thumbnail
    def createThumb(self):
        return discord.File('./assets/embeds/aegis/hiura_no.jpg', 'image.jpg')

    # creates embed
    def createEmbed(self):
        embed = discord.Embed(title="Mihate Hiura",
                              description="**This link(s) has been flagged by:"
                              + self.getFlag()+self.makeDescription()
                              + "\n\n" "User "+self.message.author.mention
                              + " tried to send malicious links flagged by one or multiple databases and antivirus engines.**"
                              + "\n\n"
                              + "@here do **NOT** click on these link(s).",
                              color=0xFF0000)
        embed.set_thumbnail(url='attachment://image.jpg')
        return embed
