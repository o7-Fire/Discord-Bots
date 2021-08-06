import discord
import random
import time
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

TOKEN = ""
client = discord.Client()
webhook = ""

async def webhooksend(message):
    async with aiohttp.ClientSession() as session:
        wh = Webhook.from_url(webhook, adapter=AsyncWebhookAdapter(session))
        await wh.send(message)
	    
@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

latestping = 0
latestpingtime = 0
alreadysent = 0
alreadysenttime = 0
@client.event
async def on_message(message):
	global latestping, latestpingtime, alreadysent, alreadysenttime
	if message.channel.id == : #the channel webhook where you receiving the pings so you dont get pinged back
		return
	if client.user.mentioned_in(message):
		if latestping == message.author.id and (time.time() - latestpingtime) < 5:
			if (time.time() - alreadysenttime) < 5 and latestping == message.author.id:
				await webhooksend(f"Hey! Someone pinged you a lot of times.\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
			else:
				await webhooksend(f"<@{client.user.id}> Hey! Someone pinged you a lot of times.\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
			alreadysenttime = time.time()
		else:
			if random.randint(0, 1) == 1:
				await message.channel.send('ping')
			else:
				await message.channel.send('ye')
			await webhooksend(f"<@{client.user.id}> Hey! Someone pinged you.\nhttps://ptb.discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
		latestping = message.author.id
		latestpingtime = time.time()


client.run(TOKEN)
