import discord #Import Discord Library and NEVER REVEAL TOKEN which is in .env
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('$Rat'):
        await message.channel.send('Squeak!')

client.run(os.getenv('NOSHOW'))#.env hides the token and NOSHOW is the token
