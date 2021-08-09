import os
import requests
import time
import random
os.system("pip3 install discord.py-self")
try:
  import discord
  from discord import Webhook, AsyncWebhookAdapter
except:
  print("something wrong, send help")

client = discord.Client()
webhook = os.getenv("token")
listofjokes = requests.get("https://pastebin.com/raw/JUBaS8Xw").text.split("\n")
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  channel = client.get_channel(840041811384860708)
  while True:
    await channel.send(random.choice(listofjokes))
    time.sleep(300)

client.run(TOKEN)
