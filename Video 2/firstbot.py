@client.command()
async def embed(ctx):
    embed = discord.Embed(title = "Hello This is my first embed", description = "This is the description", color = discord.Colour.green()) 
    embed.add_field(name = "Field Title 1",value = "Value 1",inline = True)
    embed.add_field(name = "Field Title 2",value = "Value 2",inline = False)
    embed.add_field(name = "Field Title 3",value = "Value 3",inline = True)
    embed.add_field(name = "Field Title 4",value = "Value 4",inline = True)
    await ctx.send(embed = embed)
   
@client.command(aliases = ["uf","about","whois"])
async def userinfo(ctx, member : discord.Member = None): 
    if member == None:
        await ctx.send("You didn't mention a required argument please try again!")
    else:
        embed = discord.Embed(title = f"Info of {member.display_name}",color = discord.Colour.red())
        embed.add_field(name = "User ID",value = f"{member.id}")
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
