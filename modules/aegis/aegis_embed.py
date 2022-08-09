import discord


class AegisEmbed:
    """Creates warning embed"""
    def __init__(self, aegis, message):
        """Stores aegis embed information"""
        # aegis class
        self.aegis = aegis
        # command issuer message class
        self.message = message

    def get_flag(self):
        """Returns aegis scanner flag"""
        flag_haus = ""
        flag_hyper = ""
        flag_aipdb = ""

        # adds URLHaus to flag
        if len(self.aegis.urlhaus) != 0:
            flag_haus = "\nURLHaus Malicious URL Database"

        # adds Hyperphish to flag
        if len(self.aegis.hyperphish) != 0:
            flag_hyper = "\nHyperphish Phishing URL Database"

        # adds Hyperphish to flag
        if len(self.aegis.abuseipdb) != 0:
            flag_aipdb = "\nAbuseIPDB IP Reputation Center"

        return flag_haus + flag_hyper + flag_aipdb

    def make_description(self):
        """Returns aegis embed description"""
        desc_haus = []
        desc_hyper = []
        desc_aipdb = []
        desc_haus_str = ""
        desc_hyper_str = ""
        desc_aipdb_str = ""

        # adds URL + threat to URLHaus array
        for index,i in enumerate(self.aegis.urlhaus):
            desc_haus.append("\n\nURL: "+self.aegis.urlhaus[index].url
                            + "\nThreat: "
                            + self.aegis.urlhaus[index].threat)

        # adds URL + threat to hyperphish array
        for index,i in enumerate(self.aegis.hyperphish):
            desc_hyper.append("\n\nURL: "+self.aegis.hyperphish[index].url
                             + "\nThreat: Phishing Link")

        # adds URL + details to abuseipdb array
        for index,i in enumerate(self.aegis.abuseipdb):
            desc_aipdb.append("\n\nURL: "+self.aegis.abuseipdb[index].domain
                             + "\nIP: "+self.aegis.abuseipdb[index].ip
                             + "\nAbuse Confidence Score: "
                             + str(self.aegis.abuseipdb[index].abuse_confidence)
                             + "\nCountry: "
                             + self.aegis.abuseipdb[index].country
                             + "\nReports: "
                             + str(self.aegis.abuseipdb[index].total_reports)
                             + "\nIP Type: "+self.aegis.abuseipdb[index].ip_type)
        # converts array to string
        desc_haus_str = "".join(desc_haus)
        # converts array to string
        desc_hyper_str = "".join(desc_hyper)
        desc_aipdb_str = "".join(desc_aipdb)
        return desc_haus_str + desc_hyper_str + desc_aipdb_str

    # creates embed thumbnail
    def create_thumb(self):
        """Returns aegis embed thumbnail"""
        return discord.File('./assets/embeds/aegis/hiura_no.jpg', filename = 'image.jpg')

    # creates embed
    def create_embed(self):
        """Returns aegis embed"""
        embed = discord.Embed(description="**This link(s) has been flagged by:"
                              + self.get_flag()+self.make_description()
                              + "\n\n" "User "+self.message.author.mention
                              + " tried to send malicious links flagged by one or multiple databases and antivirus engines.**"
                              + "\n\n"
                              + "@here do **NOT** click on these link(s).",
                              color=0xFF0000)
        embed.set_author(name="Mihate Hiura")
        embed.set_footer(text="© Rinlabs 2022")
        embed.set_thumbnail(url='attachment://image.jpg')
        return embed
