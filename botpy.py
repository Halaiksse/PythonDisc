 # bot.py
from random import randrange
import discord
from discord.ext import commands # This is just an extension to make commands a lot easier
import requests
import math
import random



bot = commands.Bot(command_prefix=".", help_command=None)


@bot.event
async def on_ready(): 
    print("Logged in successfuly as " + bot.user.name)

@bot.command() 
async def isOnline(ctx):
    await ctx.send("I am online !")

@bot.command()
async def MassPing(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    for x in range(10):
        await ctx.send( str(member.mention))


@bot.command(aliases=['fuckinghelpme', 'help'])
async def Help(ctx):
    embed1=discord.Embed(
        title="Help Page",
        color=discord.Color.blue())
   
    embed1.add_field(name="__.isOnline__", value="Sends a message if the bot is online.", inline=False)
    embed1.add_field(name="__.Help__", value="I think you can figure out this one by yourself.", inline=False)
    embed1.add_field(name="__.HowSus__", value="How sus am I ?", inline=False)
    embed1.add_field(name="__.MassPing__", value="Sends 10 ping to someone", inline=False)
    await ctx.send(embed=embed1)

@bot.command(aliases=['howsus', 'Howsus'])
async def HowSus(ctx):
    susrate = randrange(0, 101)
    author = ctx.message.author

    await ctx.send(  str(author.mention) + " is " + str(susrate) + " percent sus.")
# Local file containing the API key
Fileapi = open("c:\\python\\API.txt", "r")
APILIST = []
APILIST = Fileapi.readlines()



# This just runs our bot using a local file containing the API key.
bot.run(APILIST[0]) 
