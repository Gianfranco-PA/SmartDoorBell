import json
from decouple import config

TOKEN=config('TOKEN_BOT')
ADMIN=config('ADMIN_ID')
ALARM_DIR=config('ALARM_SOUND_DIR')

LIST_IDENTIFIER=[]
with open("list_home.json","r") as data:
    LIST_IDENTIFIER=json.load(data)
