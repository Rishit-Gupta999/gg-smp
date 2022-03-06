import imp
from logging import fatal
from socket import CAN_BCM_TX_ANNOUNCE
import disnake
from disnake import AllowedMentions, Intents, channel
from disnake import embeds
from disnake.embeds import Embed
import asyncio
from disnake.ext import commands
import datetime
import time
import os
import re
from disnake import Member
from disnake.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request
from disnake.ext.commands.bot import Bot
from disnake.ext.commands.converter import EmojiConverter
from disnake.ext.commands.core import command
from disnake.utils import get
from disnake import TextChannel
from disnake import ui
import sys, traceback
import json

from psutil import users
from mcstatus import MinecraftBedrockServer
from pretty_help import PrettyHelp
from dotenv import load_dotenv
load_dotenv()

from disnake.ext.commands.errors import CheckAnyFailure

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
menu = DefaultMenu(page_left="🔼", page_right="🔽", remove="⏹", active_time=15)
bot = commands.Bot(command_prefix="!",test_guilds=[817003562663149578], intents=intents, case_insensitive=True, help_command=PrettyHelp(menu=menu))


initial_extensions = ['cogs.moderation']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# @bot.command()
# async def ping(ctx):
#     before = time.monotonic()
#     message = await ctx.send("Pong!")
#     ping = (time.monotonic() - before) * 1000
#     await message.edit(content=f"Pong!  `{int(ping)}ms`")


#CALCULATOR
# @bot.slash_command(description="Adds two numbers.") 
# async def add(ctx,a:float, b:float):
#     """slashcmd desc
#     Parameters
#     ----------
#     a: Number 1
#     b: Number 2
#     """
#     await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

# @bot.slash_command(description="Subtracts two numbers.") 
# async def sub(ctx,a:float,b:float): 
#     await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

# @bot.slash_command(description="Multiplies two numbers.") 
# async def multi(ctx,a:int,b:int): 
#     await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

# @bot.slash_command(description="Divides two numbers.") 
# async def divide(ctx,a:int,b:int): 
#     await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B

# @bot.slash_command(description="Find the square of a number.")
# async def square(ctx,a:int):
#     await ctx.send(f"{a*a}") #Multilies A by itself

# @bot.command()
# async def check(ctx):
#     server = MinecraftBedrockServer.lookup("RiAKG.aternos.me:34624")
#     status = server.status()
#     embed = disnake.Embed(title="Status of GG SMP", description=f" **Edition -** `Bedrock`\n **Version -** `1.18`\n **Players in game -** `{status.players_online}`\n **Maximum Players -** `{status.players_max}`", color=ctx.author.color)
#     embed.set_thumbnail(url="https://media.discordapp.net/attachments/885185426741141504/921090028204085268/sjhnjkdbc.gif")
#     embed.set_footer(text="If Max players = 1 → Server is offline 🔴\nIf Max players = 20 → Server is online 🟢")
#     await ctx.send(embed=embed)


# @bot.slash_command(description="Monke")
# async def hhgg(ctx):
#     embed = disnake.Embed(title="SERVER RULES", color=disnake.Color.blue())
#     embed.add_field(name="Minecraft Server Rules", value="**1.** Don't steal anyone's item or opening someone chest without their permission is not allowed. \n""**2.** Be like a real warrior! Don't attack on someone without making them aware of it.\n""If you don't follow the above point and directly attack then its __responsibility of other players nearby to kill the player who is breaking this rule__.\n""**3.** If someone hits you by mistake then don't hit him back, this leads in a conflict.\n""**4.** Everyone have to contribute in public builds.\n""**5.** Do not damage property of others.\n""**6.** Mass use of **TNT** is strictly prohibited. Even in debris mining make sure you call a metting before going to mine debris with **TNT**.\n""**7.** Make sure you sleep when everyone is sleeping, if you are in a serious condition and can't sleep then leave the server and rejoin.", inline=False)
#     embed.add_field(name="Disnakedisnake Server Rules", value="There will be no rules in this disnake server and no automod. But still don't break the basic rules.", inline=False)
#     embed.add_field(name="SERVER INFO", value="**Server IP** - `RiAKG.aternos.me`\n""**Port** - `34624`\n", inline=False)
#     embed.add_field(name="SERVER FAQ", value="Server is not online for 24/7, You can check staus of server by typing `!check`. If server is offline then you can ask <@&880915882895872080> to turn it back on.", inline=False)

#     await ctx.send(embed=embed)

# @bot.slash_command(description="About me.")
# async def about(ctx):
#     embed = disnake.Embed(title="GG SMP", description= "Official Bot of GG SMP!", color=disnake.Color.red())
#     embed.add_field(name="**Developed by -**", value="Rishit Gupta")

#     await ctx.send(embed=embed)

# @bot.slash_command(description="Shows server information.")
# async def serverinfo(ctx):
#   name = str(ctx.guild.name)
#   description = str(ctx.guild.description)

#   owner = "**AKG#1234**"
#   id = str(ctx.guild.id)
#   region = str(ctx.guild.region)
#   memberCount = str(ctx.guild.member_count)

#   icon = str(ctx.guild.icon_url)
   
#   embed = disnake.Embed(
#       title=name + " Server Information",
#       description=description,
#       color=disnake.Color.blue()
#     )
#   embed.set_thumbnail(url=icon)
#   embed.add_field(name="Owner", value=owner, inline=True)
#   embed.add_field(name="Server ID", value=id, inline=True)
#   embed.add_field(name="Region", value=region, inline=True)
#   embed.add_field(name="Member Count", value=memberCount, inline=True)

#   await ctx.send(embed=embed)

    
# @bot.slash_command(description="Seached on youtube for a given query.")
# async def youtube(ctx, *, search):
#     query_string = parse.urlencode({'search_query': search})
#     html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
#     search_content= html_content.read().decode()
#     search_results = re.findall(r'\/watch\?v=\w+', search_content)
#     #print(search_results)
#     await ctx.send("Here's what I found" ' ' 'https://www.youtube.com' + search_results[0])


#MODERATION
# @bot.command()
# @commands.has_permissions(kick_members=True)
# async def kick(ctx, member: disnake.Member):
#     await member.kick()
#     await ctx.send(f"**{member.name}** has been kicked by **{ctx.author.name}**!")
# async def kick_error(ctx, error):
#     if isinstance(error, MissingPermissions):
#         text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#         await bot.send_message(ctx.message.channel, text)

@bot.event
async def on_ready():
    print('GG is ready.')

bot.run(os.getenv('TOKEN'))