from telethon.sync import TelegramClient
import csv



def get_mmbrs(USERNAME, API_ID, API_HASH, GROUPS):
    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()

    for group in GROUPS:
      
        all_participants = []
        all_participants = client.get_participants(group) #get all members
        
        
        file_name = group +'_members.csv'
        with open(file_name, "w", encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username', 'group'])
            for user in all_participants:
                writer.writerow([user.username,  group])     
 
            
