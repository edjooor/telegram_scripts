from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import csv

def get_msges(USERNAME, API_ID, API_HASH, GROUPS):
    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()
    for group in GROUPS:
        file_name = group + '_chat_history.csv'
        offset_id = 0
        limit = 100
        all_messages = []
        total_messages = 0
        total_count_limit = 0
        
        while True:
            history = client(GetHistoryRequest(
                peer=group,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.message)
            offset_id = messages[len(messages) - 1].id
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break
            
         
            with open(file_name, "w", encoding="UTF-8") as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                for message in all_messages:
                    writer.writerow([message])  
           