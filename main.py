#!/usr/bin/python3
from settings import DISCORD_TOKEN
from mafia import Mafia

m = Mafia()
m.run(DISCORD_TOKEN)
