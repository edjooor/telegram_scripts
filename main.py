import configparser
from scripts import send_message
from scripts import join_channels
from scripts import do_search
from scripts import get_group_members
from scripts import get_message_history
from scripts import get_username_by_phone


config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

phone = config['Telegram']['phone']
username = config['Telegram']['username']


#LOOK FOR KEY WORD:

key_world_for_search = ''
do_search.search_chnls(username, api_id, api_hash, key_world_for_search)


#JOIN CHANNELS:

channels_to_join = ('', '')
join_channels.join_chnls(username, api_id, api_hash, channels_to_join)


#MESSAGE SEND:

group_names = ['', '']
message = ' '
send_message.send_msg(username, api_id, api_hash, group_names, message)


#PARTICIPANTS OF GROUP TO CSV:

groups_members_to_get = ['', '']
get_group_members.get_mmbrs(username, api_id, api_hash, groups_members_to_get)


#GET MESSAGE HISTORY FROM GROUPS TO CSV:

get_history_from_groups = ['', '']
get_message_history.get_msges(username, api_id, api_hash, get_history_from_groups)


#USERNAME GET BY PHONE TO CSV:

phone_numbers_to_search = ['+', '+', '+']
get_username_by_phone.get_username(username, api_id, api_hash, phone_numbers_to_search)