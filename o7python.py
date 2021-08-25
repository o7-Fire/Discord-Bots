import asyncio
import discord
import subprocess
import time
import re
import os
import threading

TOKEN = ""
client = discord.Client()
val = 0
whitelisted = [854577311810060288, 450360653094584340, 394771663155101727, 761484355084222464, 710316824797118544, 829381385801957397] #dont want your pc to get hijacked

def preventinfiniteloop():
  didthecommandwork = 0
  time.sleep(300)
  while True:
    time.sleep(1)
    if didthecommandwork == 0:
      try:
        os.execv(sys.executable, ['python'] + sys.argv)
        didthecommandwork = 1
      except:
        didthecommandwork = 0

startthefunctiontopreventinfiniteloop = threading.Thread(target=preventinfiniteloop)
startthefunctiontopreventinfiniteloop.start()

def findcharlength(txtfile):
    with open(txtfile) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
    return characters
    
    
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
  if message.author.bot:
    return
  if message.content == "test":
    await message.channel.send("yeah im alive")
  if message.author.id in whitelisted:
    nothingsdu8infgevusybt = 0
  else:
    return
  if message.content == "enablepr":
    global val
    if val != 0:
        val = 0
        f = open("val.txt", "w")
        f.write(str(val))
        f.close()
        await message.channel.send("printing each line disabled")
    else:
        val = 1
        f = open("val.txt", "w")
        f.write(str(val))
        f.close()
        await message.channel.send("printing each line enabled")
  if message.content.startswith("pip3"):
    packagetoinstall = message.content.split("pip3 ")[1]
    await message.channel.send("installing : " + packagetoinstall)
    os.system("pip3 install " + packagetoinstall)
    await message.channel.send("done installing " + packagetoinstall)
  if message.content.startswith("py"):
    if "@everyone" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if "@here" in message.content:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no")
        return
    if 1 == 1:
        file_object  = open("pee.py", "w+")
        removedpy = message.content.replace("py", "", 1)
        calc = [m.start() for m in re.finditer("input()", removedpy)]
        for i in range(len(calc)):
            try:
                await message.channel.send("input:")
                msg = await client.wait_for("message", timeout=30)  # 30 seconds to reply
                removedpy = removedpy.replace("input()", str(msg.content), 1)
            except asyncio.TimeoutError:
                await message.channel.send("Sorry, you didn't reply in time!")
                return
        file_object.write(removedpy)
        file_object.close()
        std = subprocess.run(['python3', 'pee.py'], capture_output=True, text=True)
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                if len(std.stdout) >= 2000:
                    with open("result.txt", "w") as file:
                        file.write(std.stdout)
                    with open("result.txt", "rb") as file:
                        await message.channel.send("<@" + str(message.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                elif std.stdout == None:
                    await message.cannel.send("<@" + str(message.author.id) + "> no response")
                else:
                    await message.channel.send("<@" + str(message.author.id) + ">")
                    await message.channel.send(std.stdout.replace("@everyone", "@ everyone").replace("@here", "@ here"))
        else:
            await message.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
            await message.channel.send("Tracebacks:\n " + str(std.stderr))

client.run(TOKEN)
