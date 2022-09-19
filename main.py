import discord
from replit import db

client = discord.Client()

def update_testlicence(licence):
  if "testlicence" in db.keys():
    testlicence = db["testlicence"]
    testlicence.append(licence)
    db["testlicence"] = testlicence
  else:
    db["testlicence"] = [licence]

def delete_licence(index):
  testlicence = db["testlicence"]
  if len(testlicence) > index:
    del testlicence[index]
  db["testlicence"] = testlicence

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith(".addcode"):
    testlicence = []
    if "testlicence" in db.keys():
      testlicence = db["testlicence"]
    new_licence = msg.split(".addcode ",1)[1]
    try:
      index = testlicence.index(new_licence)
      await message.channel.send("This licence already exists.")
    except ValueError:
      update_testlicence(new_licence)
      await message.channel.send("New licence added.")

  if msg.startswith(".redeem"):
    testlicence = []
    if "testlicence" in db.keys():
      testlicence = db["testlicence"]
    licence = msg.split(".redeem ",1)[1]
    try:
      index = testlicence.index(licence)
      delete_licence(index)
      await message.channel.send("Success")
    except ValueError:
      await message.channel.send("Failure")

  if msg.startswith("$del"):
    testlicence = []
    if "testlicence" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_licence(index)
      testlicence = db["testlicence"]
    await message.channel.send(testlicence)

  if msg.startswith("$list"):
    testlicence = []
    if "testlicence" in db.keys():
      testlicence = db["testlicence"]
    await message.channel.send(testlicence)
    
client.run('OTkyNjA4ODEyMjAyNzIxMzUy.GsywJb.tK93dtRpNXF64H4F0CAx3esoXGwY54RU46NSUQ')