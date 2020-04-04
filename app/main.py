import glob

from app.utils import load_config
from telebot import TeleBot, types

bot = TeleBot(load_config()['config']['props']['token'])


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='CLick me', callback_data='add')
    markup.add(button)
    bot.send_message(chat_id=message.chat.id, text='Some text', reply_markup=markup)


@bot.message_handler(content_types=['document'])
def load_doc(message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    file = bot.download_file(file_info.file_path)
    with open(f'../files/{file_name}', 'wb') as new_file:
        new_file.write(file)
    bot.reply_to(message, 'done')


@bot.message_handler(commands=['show_files'])
def show_files(message):
    bot.reply_to(message, [path for path in glob.glob("../files/*.*")])


def main():
    bot.polling()


if __name__ == '__main__':
    main()
