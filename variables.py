from firebase_admin import credentials,initialize_app
import json
from decouple import config

TOKEN=config('TOKEN_BOT')
ADMIN=config('ADMIN_ID')
ALARM_DIR=config('ALARM_SOUND_DIR')

#FIREBASE
CREDENTIAL_DIR=config('CREDENTIAL_DIR')
GS_DIR=config("GS_DIR")
CRED = credentials.Certificate(CREDENTIAL_DIR)
initialize_app(CRED, {'storageBucket': GS_DIR})

LIST_IDENTIFIER=[]
with open("list_home.json","r") as data:
    LIST_IDENTIFIER=json.load(data)
