from telethon import TelegramClient, events

api_id = 15328151
api_hash = 'abd07c261c86f3a7919e4984ac69698b'


client = TelegramClient('anon', api_id, api_hash)

channels = ['@test2111']

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()