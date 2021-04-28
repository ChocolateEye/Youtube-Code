import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!!",intents=intents) 

@client.event 
async def on_ready():
    print("The bot is online") 

@client.command(aliases = ["hi","hello"]) 
async def Hi(ctx):
    await ctx.send("Hi there! :wave:")

@client.command() 
async def hru(ctx): 
    await ctx.send("I am fine! What about you?")

@client.event
async def on_member_join(member):
    channel = client.get_channel(834104515878846475)
    embed = discord.Embed(title=f"{member.display_name} has joined the server!", description = f"Welcome to the server!", colour = 0x80ff00)
    embed.add_field(name = "Username : ", value = f"{member.display_name}")
    embed.add_field(name = "Discord ID : ", value = f"{str(member.id)}")
    embed.add_field(name = "Account Created at : ", value = f"{member.created_at}")
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url = "https://media3.giphy.com/media/fU4elxKlRsulB4Jy7w/200.gif")
    embed.set_footer(text = channel.guild, icon_url=channel.guild.icon_url)
    await channel.send(embed = embed)
