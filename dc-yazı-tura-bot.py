import discord
import random

TOKEN = 'degisken icin token'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!yat':
        result = random.choice(['Yazı', 'Tura'])
        await message.channel.send(f'{message.author.mention} {result} attı!')

client.run(TOKEN)
