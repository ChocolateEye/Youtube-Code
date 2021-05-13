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
async def bye(ctx):
    await ctx.send("Bye!")

@client.command()
async def ctx(ctx):
    print(ctx)
    print(ctx.author)
    print(ctx.message.created_at)
    print(ctx.guild)
    print(ctx.channel)

@client.command() 
async def hru(ctx): 
    await ctx.send(f"I am fine! What about you {ctx.author} in channel {ctx.channel} in the server {ctx.guild}?")

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

client.run("bot token here")
