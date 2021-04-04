import discord #Import Discord Library and NEVER REVEAL TOKEN which is in .env
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable"]
starter_encouragments = ["Cheer Up!", "Hang in there." "You are a great person"]

if "responding" not in db.keys():
    db["responding"] = True

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)

def update_encouragments(encouraging_message):
    if "encouragements" in db.keys():
        encouragments = db["encouragements"]
        encouragments.append(encouraging_message)
        db["encouragements"] = encouragments
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
    encouragments = db["encouragements"]
    if len(encouragments) > index:
        del encouragments[index]
        db["encouragements"] = encouragments

#End of Functions, Start of Main
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #Don't Respond to yourself
        return 
    
    msg = message.content

    if msg.lower().startswith('$rat'):
        await message.channel.send('Squeak')

    if msg.lower().startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if db["responding"]:
        options = starter_encouragments
        if "encouragements" in db.keys():
            options = options.extend(db["encouragements"])

        if any(word in msg.lower() for word in sad_words):
            await message.channel.send(random.choice(options))    

    if msg.lower().startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragments(encouraging_message)
        await message.channel.send("New encouraging message added.")        

    if msg.lower().startswith("$ping"):
        name = msg9
        await message.channel.send("@" + )

    if msg.lower().startswith("$del"):
        encouragments = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])#No Space because it is casted to int
            delete_encouragment(index)
            encouragments = db["encouragements"]
        await message.channel.send(encouragments)  

    if msg.lower().startswith("$list"):
        encouragments = []
        if "encouragements" in db.keys():
            encouragments = db["encouragements"]
        await message.channel.send(encouragments)

    if msg.lower().startswith("$responding"):
        value = msg.split("$responding ",1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('NOSHOW'))#.env hides the token and NOSHOW is the token