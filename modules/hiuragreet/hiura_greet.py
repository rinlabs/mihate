import discord

def greet_file():
    """Returns greet embed thumbnail"""
    return discord.File('./assets/embeds/hiuraroll/SSR/012.jpg', 'image.jpg')


def greet_embed(ctx):
    """Returns join embed """
    embed = discord.Embed(color=0xFFFF96,description="**Hello,  "
                              +ctx.author.mention
                              +" !"
                              +"\n"
                              +"(＾▽＾)**")
    embed.set_author(name="Mihate Hiura")
    embed.set_footer(text="© Rinlabs 2022")
    embed.set_thumbnail(url='attachment://image.jpg')
    return embed

