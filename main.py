import os
import telebot
from dotenv_vault import load_dotenv
from uwu import english_to_uwu

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# handle uwu command
@bot.message_handler(commands=['uwu'])
def uwuify_message(message):
    bot.send_message(message.chat.id, "uwuify youw message!")
    bot.register_next_step_handler(message, translate_uwu)
def translate_uwu(message):
    res = english_to_uwu(message.text)
    bot.send_message(message.chat.id, res)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()