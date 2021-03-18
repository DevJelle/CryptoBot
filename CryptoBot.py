import discord
import asyncio
#import time
from discord.ext import commands, tasks
from datetime import datetime, date, time, timezone

from lxml import html
from bs4 import BeautifulSoup
import requests

from random import randint

from keep_alive import keep_alive

client = commands.Bot(command_prefix = '-')

client.remove_command("help")



async def mainStatus():
    
    cryptoChannel = client.get_channel(821018785133232128)
    timestamp = datetime.now()

    rStatus = requests.get('https://8b380bb9-5237-4ef8-a0cf-3a6b831dba72.id.repl.co/')
    statusSoup = BeautifulSoup(rStatus.content, "html.parser")
    status = statusSoup.find_all(text=True)
    
    if 'Hello. I am alive!' in status:
         message = await cryptoChannel.send('**'+"CryptoBot is currently OPERATING"+'**'+" \U0001f7e2"+" *More info here:* https://stats.uptimerobot.com/oX9yvSXWMD/787507457 " 
         + "                *Last updated:* " + str(timestamp.strftime(r"%Y-%m-%d %H:%M:%S")))
    else:
        message = await cryptoChannel.send('**'+"CryptoBot is currently DOWN"+'**'+" \U0001f534"+" *More info here:* https://stats.uptimerobot.com/oX9yvSXWMD/787507457 "
        + "                 *Last updated:* " + str(timestamp.strftime(r"%Y-%m-%d %H:%M:%S")))

    await asyncio.sleep(300)
    await message.delete()

@client.event
async def on_ready(): 
    print('Bot is ready.')
    while True:
        await mainStatus()
        await asyncio.sleep(1)
        

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

@client.command()
async def status(ctx):
    rStatus = requests.get('https://8b380bb9-5237-4ef8-a0cf-3a6b831dba72.id.repl.co/')
    statusSoup = BeautifulSoup(rStatus.content, "html.parser")
    status = statusSoup.find_all(text=True)
    
    if 'Hello. I am alive!' in status:
        await ctx.send('**'+"CryptoBot is currently OPERATING"+'**'+" \U0001f7e2"+" *More info here:* https://stats.uptimerobot.com/oX9yvSXWMD/787507457 ")
    else:
        await ctx.send('**'+"CryptoBot is currently DOWN"+'**'+" \U0001f534"+" *More info here:* https://stats.uptimerobot.com/oX9yvSXWMD/787507457 ")

    

keep_alive()
client.run('token')