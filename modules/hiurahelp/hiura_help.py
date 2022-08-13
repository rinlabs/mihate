import discord

def help_file():
    """Returns join embed thumbnail"""
    return discord.File('./assets/embeds/hiuraroll/Elite/010.jpg', 'image.jpg')

# creates embed
def help_embed(prefix):
    """Returns help embed"""
    embed = discord.Embed(color=0xFF0064)
    embed.add_field(name="__**Hiuraroll**__", value="Spawns a random Hiura"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"hiuraroll**",
                              inline=False)
    embed.add_field(name="__**Neko**__", value="Spawns a random cat image"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"neko**",
                              inline=False)
    embed.add_field(name="__**Hiura Greet**__", value="Greets the user"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"greet**",
                              inline=False)
    embed.add_field(name="__**Lineart**__", value="Spawns a random lineart"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"lineart**",
                              inline=False)
    embed.add_field(name="__**Coinflip**__", value="Flips a coin"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"coinflip**",
                              inline=False)
    embed.add_field(name="__**Help**__", value="Invokes this message"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"help**",
                              inline=False)
    embed.set_author(name="Mihate Hiura")
    embed.set_footer(text="© Rinlabs 2022")
    embed.set_thumbnail(url='attachment://image.jpg')
    return embed
    