from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time



def join_chnls(USERNAME, API_ID, API_HASH, CHANNELS):
  
    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()
        
    for channel in CHANNELS:
        client(JoinChannelRequest(channel))
        time.sleep(5)
        
