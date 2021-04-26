 # bot.py
from random import randrange
import discord
from discord.ext import commands # This is just an extension to make commands a lot easier
import requests
import math
import hypixel


bot = commands.Bot(command_prefix=".", help_command=None) # You can set your prefix to be anything you desire!


@bot.event
async def on_ready(): # This function will be run by the discord library when the bot has logged in
    print("Logged in successfuly as " + bot.user.name)

@bot.command() 
async def isOnline(ctx):
    await ctx.send("I am online !")





@bot.command(aliases=['fuckinghelpme', 'help'])
async def Help(ctx):
    embed1=discord.Embed(
        title="Help Page",
        color=discord.Color.blue())
   
    embed1.add_field(name="__.isOnline__", value="Sends a message if the bot is online.", inline=False)
    embed1.add_field(name="__.Help__", value="I think you can figure out this one by yourself.", inline=False)
    embed1.add_field(name="__.HowSus__", value="How sus am I ?", inline=False)
    await ctx.send(embed=embed1)

@bot.command()
async def HowSus(ctx):
    susrate = randrange(0, 101)
    author = ctx.message.author

    await ctx.send("You are " + str(susrate) + " percent sus.")

@bot.command()
async def profile(ctx, name):
    level = hypixel.get_level(name) # This is a reference the function we just created in hypixel.py
    karma = hypixel.get_karma(name)
    
    if level is None: # Remember back in hypixel.py we returned 'None' if the API couldn't find a player
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)") # This just sends a message to the channel the command was sent in from the bot
    else: # We know that we found a player now because level is not None
        embed2=discord.Embed(
            title=f"Profile of {name}",
            color=discord.Color.purple())
        embed2.add_field(name="__Level__", value=f"{level}", inline=False)
        embed2.add_field(name="__Karma__", value=f"{karma}", inline=False)
        
        await ctx.send(embed=embed2)
        



    

Fileapi = open("c:\\python\\API.txt", "r")
APILIST = []
APILIST = Fileapi.readlines()



# This just runs our bot
bot.run(APILIST[1]) 
