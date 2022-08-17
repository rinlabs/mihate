import time
import os
import logging
from random import seed, randint
import discord
from dotenv import load_dotenv
from urlextract import URLExtract
from art import text2art, randart
from discord.ext import commands

from modules.cli.clear_screen import clear
from modules.urlprocessing.url_processing import url_check
from modules.hiuraroll.roll_embed import RandomHiuraEmbed
from modules.dbcon.sqlite_con import make_ownership
from modules.aegis.aegis_embed import AegisEmbed
from modules.aegis.aegis import Aegis
from modules.hiurahelp.hiura_help import help_file,help_embed
#from modules.memberjoin.join_greet_embed import join_file,join_embed
from modules.hiuragreet.hiura_greet import greet_file,greet_embed
from modules.nekomimi.nekomimi import neko_embed

# load_dotenv
load_dotenv('.env')
#  logging
logging.basicConfig(level=logging.INFO)
# prefix
mihate = commands.Bot(command_prefix=os.getenv('PREFIX'),
                            activity=discord.Activity(
                                type=discord.ActivityType.listening,
                                name=(os.getenv('PREFIX') + "help"),
                             intents=discord.Intents().all))

# remove default help command
mihate.remove_command('help')


# on-ready console notification & bot presence
@mihate.event
async def on_ready():
    """"On-ready console text"""
    clear()
    print(text2art("mihate", font='tarty1'))
    print("Logged in as {0.user}".format(mihate))


# AEGIS anti spam link protection
@mihate.event
async def on_message(message):
    """"Checks message for malicious link"""
    # checks if the author is the bot itself
    if message.author == mihate.user:
        return
    else:
        if URLExtract().has_urls(url_check(message.content)) is True:
            aegis_scan = Aegis(message.content)
            if aegis_scan.threat_value != 0:
                aegis_result_embed = AegisEmbed(aegis_scan, message)
                await message.channel.send(file=aegis_result_embed.create_thumb(),
                                           embed=aegis_result_embed.create_embed())
                await mihate.process_commands(message)
        await mihate.process_commands(message)


# new member greeting
#@mihate.event
#async def on_member_join(member, guild):
#    """"Greets new member"""
#    print('Detected new member join')
#    await mihate.get_channel(guild.channel).send(file=join_file(), embed=join_embed(member))
#    await mihate.process_commands(member.message)


# help override
@mihate.command()
async def help(ctx):
    """"Help override"""
    embed = help_embed(os.getenv('PREFIX'))
    await ctx.channel.send(file=help_file(),
                                embed=embed)


# greet command
@mihate.command()
async def greet(ctx):
    """"Simple greeting"""
    await ctx.channel.send(file=greet_file(),
                               embed=greet_embed(ctx))


# random lineart command
@mihate.command()
async def lineart(ctx):
    """"Random lineart"""
    await ctx.channel.send(randart())


# random hiura image
@mihate.command()
async def hiuraroll(ctx):
    """"Hiuraroll gacha minigame"""
    # sets random seed number based on system time
    seed(round(time.time() * 1000))
    rng = randint(0, 1000)

    if 0 < rng < 550:
        common_hiura = RandomHiuraEmbed('Common', ctx)
        await ctx.channel.send(file=common_hiura.create_file(),
                               embed=common_hiura.create_embed())
        make_ownership(common_hiura.user_id, common_hiura.rng, 'Common')
    elif 550 < rng < 750:
        rare_hiura = RandomHiuraEmbed('Rare', ctx)
        await ctx.channel.send(file=rare_hiura.create_file(),
                               embed=rare_hiura.create_embed())
        make_ownership(rare_hiura.user_id, rare_hiura.rng, 'Rare')
    elif 750 < rng < 850:
        elite_hiura = RandomHiuraEmbed('Elite', ctx)
        await ctx.channel.send(file=elite_hiura.create_file(),
                               embed=elite_hiura.create_embed())
        make_ownership(elite_hiura.user_id, elite_hiura.rng, 'Elite')
    elif 850 < rng < 975:
        ssr_hiura = RandomHiuraEmbed('SSR', ctx)
        await ctx.channel.send(file=ssr_hiura.create_file(),
                               embed=ssr_hiura.create_embed())
        make_ownership(ssr_hiura.user_id, ssr_hiura.rng, 'SSR')
    elif 975 < rng < 1000:
        ur_hiura = RandomHiuraEmbed('UR', ctx)
        await ctx.channel.send(file=ur_hiura.create_file(),
                               embed=ur_hiura.create_embed())
        make_ownership(ur_hiura.user_id, ur_hiura.rng, 'UR')


# coinflip
@mihate.command()
async def coinflip(ctx):
    """"Coinflip"""
    seed(round(time.time() * 1000))
    rng = randint(0, 1)
    if rng == 0:
        await ctx.channel.send("Heads!")
    elif rng == 1:
        await ctx.channel.send("Tails!")

# nekomimi
@mihate.command()
async def neko(ctx):
    """"Get random cat image"""
    await ctx.channel.send(embed=neko_embed())


mihate.run(os.getenv('TOKEN'))
