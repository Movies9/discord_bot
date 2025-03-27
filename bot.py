import discord
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Bot token stored as an environment variable

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)
