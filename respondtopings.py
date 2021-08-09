# this responds to pings instantly and pings you in a seperate server for you to respond yourself
# not sure purpose

import keep_alive
keep_alive.keep_alive()
import os
import random
import time
import aiohttp
os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
except:
  print("something wrong, send help")

TOKEN = os.getenv("webhook")
client = discord.Client()
webhook = os.getenv("token")
blacklisted_users = [698318981282529352]
mode = 1
#0 = get pings but in different server
#1 = dont get pings at all
#2 = counter ping to annoy

async def webhooksend(message):
    async with aiohttp.ClientSession() as session:
        wh = Webhook.from_url(webhook, adapter=AsyncWebhookAdapter(session))
        await wh.send(message)
	    
async def sendformat(message, alotoftimes, pinguser):
  if alotoftimes:
    if pinguser:
      await webhooksend(f"<@{client.user.id}> Hey! Someone pinged you a lot of times.\nName: {message.author.name} (<@{message.author.id}>)\nServer: {message.guild.name}\nChannel: {message.channel.name}\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
    else:
      await webhooksend(f"Hey! Someone pinged you a lot of times.\nName: {message.author.name} (<@{message.author.id}>)\nServer: {message.guild.name}\nChannel: {message.channel.name}\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
  else:
    if pinguser:
      await webhooksend(f"<@{client.user.id}> Hey! Someone pinged you.\nName: {message.author.name} (<@{message.author.id}>)\nServer: {message.guild.name}\nChannel: {message.channel.name}\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
    else:
      await webhooksend(f"Hey! Someone pinged you.\nName: {message.author.name} (<@{message.author.id}>)\nServer: {message.guild.name}\nChannel: {message.channel.name}\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

latestping = 0
latestpingtime = 0
alreadysent = 0
alreadysenttime = 0
@client.event
async def on_message(message):
  global latestping, latestpingtime, alreadysent, alreadysenttime, mode
  if message.channel.id == 873214338436063352 or message.author.id in blacklisted_users or not client.user.mentioned_in(message):
    return
  if mode == 0:
    if latestping == message.author.id and (time.time() - latestpingtime) < 5:
      if (time.time() - alreadysenttime) < 5 and latestping == message.author.id:
        sendformat(message, True, False)
      else:
        sendformat(message, True, True)
      alreadysenttime = time.time()
    else:
      await message.channel.send(".")
      sendformat(message, False, True)
    latestping = message.author.id
    latestpingtime = time.time()
  elif mode == 1:
    await message.ack()
    if latestping == message.author.id and (time.time() - latestpingtime) < 5:
      if (time.time() - alreadysenttime) < 5 and latestping == message.author.id:
        sendformat(message, True, False)
      else:
        sendformat(message, True, True)
      alreadysenttime = time.time()
    else:
      sendformat(message, False, False)
    latestping = message.author.id
    latestpingtime = time.time()
  elif mode == 2:
    if latestping == message.author.id and (time.time() - latestpingtime) < 5:
      if (time.time() - alreadysenttime) < 5 and latestping == message.author.id:
        sendformat(message, True, False)
      else:
        sendformat(message, True, True)
      alreadysenttime = time.time()
    else:
      await message.channel.send(f"<@{message.author.id}>")
      sendformat(message, False, False)
    latestping = message.author.id
    latestpingtime = time.time()

client.run(TOKEN)
