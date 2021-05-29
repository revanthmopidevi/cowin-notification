from decouple import config

import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events



def teleMessage(API_ID, API_HASH, PHONE, to, message):
    client = TelegramClient('session', API_ID, API_HASH)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(PHONE)
        client.sign_in(PHONE, input('Enter the code: '))
    
    try:
        # receiver = InputPeerUser('user_id', 'user_hash')
        for each in to:
            recipient = client.get_input_entity(each)
            client.send_message(recipient, message, parse_mode='html')
    except Exception as e:
        print(e);
 
    client.disconnect()