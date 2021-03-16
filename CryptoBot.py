import discord
from discord.ext import commands

from lxml import html
from bs4 import BeautifulSoup
import requests

from random import randint

from keep_alive import keep_alive

client = commands.Bot(command_prefix = '-')

client.remove_command("help")


@client.event
async def on_ready(): 
    print('Bot is ready.')

@client.command()
async def help(ctx):
    await ctx.send(ctx.author.mention + " See the #₿-crypto-bot-updates channel for more info.")

@client.command()
async def hnt(ctx):
    rHNT = requests.get('https://coinmarketcap.com/currencies/helium/')
    soupHNT = BeautifulSoup(rHNT.content, "lxml")
    hntParsed = soupHNT.find_all("div",class_= "priceValue___11gHJ")
    for value in hntParsed: 
        hntPrice = value.get_text()
    await ctx.send("The current price of 1 Helium coin = " + "**" + hntPrice + '**')

@client.command()
async def btc(ctx):
    rBTC = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
    soupBTC = BeautifulSoup(rBTC.content, "lxml")
    btcParsed = soupBTC.find_all("div",class_="priceValue___11gHJ")
    for value in btcParsed:
        btcPrice = value.get_text()
    await ctx.send("The current price of 1 Bitcoin = " + "**" + btcPrice + '**')

@client.command()
async def doge(ctx):
    rDOGE = requests.get('https://coinmarketcap.com/currencies/dogecoin/')
    soupDOGE = BeautifulSoup(rDOGE.content, "lxml")
    dogeParsed = soupDOGE.find_all("div",class_="priceValue___11gHJ")
    for value in dogeParsed:
        dogePrice = value.get_text()
    await ctx.send("The current price of 1 Dogecoin = " + "**" + dogePrice + '**')


#How sus calculator? "ඞ"
@client.command()
async def sus(ctx):
    susResult = str(randint(0,100))
    await ctx.send(ctx.author.mention + " You are " + susResult + "% " + "sus **ඞ**")

keep_alive()
client.run('token')