from telethon import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am your userbot.')
    raise events.StopPropagation

client.run_until_disconnected()
