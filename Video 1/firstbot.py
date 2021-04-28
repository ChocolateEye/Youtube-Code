import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!!")

@client.event
async def on_ready():
    print("The bot is online")

@client.command(aliases = ["hi","hello"])
async def Hi(ctx):
    await ctx.send("Hi there! :wave:")

@client.command()
async def hru(ctx):
    await ctx.send("I am fine! What about you?")

client.run("bot token here")
