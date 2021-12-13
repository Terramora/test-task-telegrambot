from time import sleep

from bot.bot import TelegramBot
from config import Config, get_config

config: Config = get_config()


def start_bot():
    bot = TelegramBot(
        token=config.telegram.token
    )
    update_id = 0
    while True:
        updates = bot.get_updates(offset=update_id)
        if 'result' in updates and updates['result']:
            for event in updates['result']:
                update_id = event['update_id'] + 1
                message = event['message']
                if 'text' in message:
                    text = message['text']
                else:
                    text = "message must be text"
                message_id = message['message_id']
                chat_id = message['chat']['id']

                bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=message_id)

        sleep(1)


start_bot()
