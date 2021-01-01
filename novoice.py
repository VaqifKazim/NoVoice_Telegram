import time
from telethon import TelegramClient, events
import re

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

# fill in your own details here
phone = '+994501234567'
username = 'Your_Telegram_Username'
# password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

# content of the automatic reply
messageText = "Do not sent voice messages, I will not receive them."

def main():
    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash)
    client.start()

    # event handler for all messages
    @client.on(events.NewMessage())
    async def handler(event):
        print("Message event occured: ", event) # log just for content debugging
        if event.is_private: # to delete only private messages, otherwise it will delete messages from group chats
            print(time.asctime(), '-', event.message)  # optionally log time and message
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            # detects type of message
            if (event.message.media.document and event.message.media.document.attributes[0] and event.message.media.document.attributes[0].voice):
                await event.delete() # deletes sent voice message
                await client.send_message(event.message.from_id, messageText) # optionally, sends automatically text message
    print(time.asctime(), '-', 'Auto-replying...')
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
