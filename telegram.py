import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import telethon.sync

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
PeerChannel
)
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

# [Telegram]
# no need for quotes

# you can get telegram development credentials in telegram API Development Tools
# api_id = Telegram-API-ID
# api_hash = Telegram-API-Hash

# # use full phone number including + and country code
# phone = Your-Telegram-Phone-Number
# username = Your-Telegram-Username


client = TelegramClient("amirda9", 7433191, "31709afde748ab8081424b4056b086e5")
client.start()
print("Client Created")
# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request("+989015241715")
    try:
        client.sign_in("+989015241715", input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))
        
        
# user_input_channel = input("enter entity(telegram URL or entity id):")
user_input_channel = "OfficialTwitterFarsi"

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel

my_channel = client.get_entity(entity)





def my():
    offset = 0
    limit = 100
    all_participants = []
    # while True:
    #     participants = client(GetParticipantsRequest(
    #     my_channel, ChannelParticipantsSearch(''), offset, limit,
    #     hash=0
    #     ))
    #     if not participants:
    #         break
    #     all_participants.extend(participants.users)
    #     offset = len(all_participants)
    # all_user_details = []
    # for participant in all_participants:
    #     all_user_details.append(
    #     {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
    #      "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})
        
    # with open('user_data.json', 'w') as outfile:
    #     json.dump(all_user_details, outfile)
    
    
    offset_id = 0
    limit = 5000
    all_messages = []
    total_messages = 0
    total_count_limit = 0
    while True:
        # print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = client(GetHistoryRequest(
            peer=my_channel,
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
            all_messages.append(message.to_dict())
            print(message.message)
            with open('history.txt', 'a') as outfile:
                # json.dump(message.message, outfile)
                outfile.writelines(message.message)
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
        
        # print(total_messages)

my()    
    



        