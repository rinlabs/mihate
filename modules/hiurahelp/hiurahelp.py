import discord

# creates embed
def helpEmbed(prefix):
    embed = discord.Embed(color=0xFFFFFF)
    embed.add_field(name="__**Hiuraroll**__", value="Spawns a random Hiura"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"hiuraroll** \n",
                              inline=False)
    embed.add_field(name="\n__**Hiura Greet**__", value="Greets the user"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"greet** \n",
                              inline=False)
    embed.add_field(name="\n__**Lineart**__", value="Spawns a random lineart"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"lineart** \n",
                              inline=False)
    
    embed.add_field(name="\n__**Help**__", value="Invokes this message"
                              + "\n\n"
                              + "Commands to type: "
                              + "\n"
                              + "**"+prefix+"help** \n",
                              inline=False)
    embed.set_author(name="Mihate Hiura")
    embed.set_footer(text="© Rinlabs 2022")
    embed.set_thumbnail(url='attachment://image.jpg')
    return embed
    