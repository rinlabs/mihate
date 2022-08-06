import discord

def joinFile():
    discord.File('./assets/embeds/hiuraroll/SSR012.jpg', 'image.jpg')


def joinEmbed(member):
    embed = discord.Embed(color=0xFFFF96)
    embed.add_field(name="**Hello, "
                              +member.mention
                              +" !**", 
                    value="Welcome to"
                              + member.guild.name
                              + "!"
                              + "\n"
                              + "Enjoy your stay here!",
                              inline=False)
    embed.set_author(name="Mihate Hiura")
    embed.set_footer(text="© Rinlabs 2022")
    embed.set_thumbnail(url='attachment://image.jpg')
    return embed