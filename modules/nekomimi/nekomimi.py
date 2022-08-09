import discord


class nekomimi:
    def __init__(self):
        self.url = "https://cataas.com/cat"
        self.thumb = "./assets/embeds/nekomimi/hiura_neko.jpg"

    # creates embed picture
    def craete_thumb(self):
        return discord.File(self.thumb, filename="image.jpg")

    # creates embed
    def create_embed(self):
        embed = discord.Embed(title="Mihate Hiura",
                              color=0x00FF00)
        embed.set_image(url=self.url)
        embed.set_thumbnail(url='attachment://image.jpg')
        return embed
