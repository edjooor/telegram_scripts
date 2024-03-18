from telethon.sync import TelegramClient
import csv
from telethon import functions, types


def get_username(USERNAME, API_ID, API_HASH, PHONE_NUMBERS):
    client = TelegramClient(USERNAME, API_ID, API_HASH)
    client.start()
    finded_users = []
    file_name = 'finded_users_by_numbers.csv'

    with open(file_name, "w", encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['phone', 'username'])  
        for phone_num in PHONE_NUMBERS: 
            contact = types.InputPhoneContact(client_id=0, phone=phone_num, first_name="name", last_name="surname")
            result = client(functions.contacts.ImportContactsRequest([contact]))
            contact_info = client.get_entity(phone_num)
            finded_users.append(contact_info.username)
            
            writer.writerow([phone_num, contact_info.username])   