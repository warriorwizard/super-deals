from telethon import TelegramClient, events
import asyncio

api_id = 15328151
api_hash = 'abd07c261c86f3a7919e4984ac69698b'

my_channel_id = 'Amazon_giveaways'
channels = ['test2111','Offerzone_Rd','Offerzone_deals']

client = TelegramClient('anon', api_id, api_hash)
print("GRAB - Started")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)
 
 
client.start()
client.run_until_disconnected()