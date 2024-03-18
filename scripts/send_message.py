import time
from telethon import TelegramClient

def send_msg(USERNAME, API_ID, API_HASH, GROUP_NAMES, MESSAGE):
    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()
    for i in range(len(GROUP_NAMES)):
        
        client.send_message(GROUP_NAMES[i], MESSAGE)
        time.sleep(5)