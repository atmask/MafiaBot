# Get needed env vars
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID')) # requires an int value

