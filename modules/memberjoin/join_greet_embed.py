import discord

def join_file():
    """Returns join embed thumbnail"""
    discord.File('./assets/embeds/hiuraroll/SSR/012.jpg', 'image.jpg')


def join_embed(member):
    """Returns join embed """
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
