from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon import functions

def search_chnls(USERNAME, API_ID, API_HASH, SEARCH):

    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()
       
    result = client(functions.contacts.SearchRequest(
        q=SEARCH,
        limit=100
    ))
    
    print(result.stringify())
    

    