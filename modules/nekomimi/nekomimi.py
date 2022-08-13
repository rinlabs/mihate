import os
import json
import requests
import discord


def query_catapi():
    """query catapi for cat images"""
    endpoint = 'https://api.thecatapi.com/v1/images/search'
    headers = {
        'x-api-key': os.getenv('CATAPI_KEY')
    }
    response = requests.request(method='GET', url=endpoint, headers=headers).json()
    return(response[0]['url'])

# creates embed
def neko_embed():
    """return cat embed"""
    embed = discord.Embed(title="**=^..^=**",
                            color=0xFFFFFF)
    embed.set_image(url=query_catapi())
    embed.set_footer(text="© Rinlabs 2022 | Cat image provided by thecatapi.com")
    return embed
