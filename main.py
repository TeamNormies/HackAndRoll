import os
import telebot
from dotenv_vault import load_dotenv
from mcel import mcelTranslate
from translation import eng_to_jap
from shakespeare import translate_to_shakespeare

load_dotenv()

TOKEN = os.getenv('TOKEN')


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['4'])
def toggleMCEL(message):
    bot.send_message(message.chat.id, "Say something!")
    bot.register_next_step_handler(message, modifyMCEL)

def modifyMCEL(message):
    output = mcelTranslate(message.text)
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['jp'])
def toggle_jp(message):
    bot.send_message(message.chat.id, "What do you want to say in Japanese?")
    bot.register_next_step_handler(message, translate_jp)

def translate_jp(msg):
    res = eng_to_jap(msg.text)
    bot.send_message(msg.chat.id, res)


@bot.message_handler(commands=['shakespeare'])
def toggle_jp(message):
    bot.send_message(message.chat.id, "Shakespeare what?")
    bot.register_next_step_handler(message, shakespeare)

def shakespeare(msg):
    res = translate_to_shakespeare(msg.text)
    bot.send_message(msg.chat.id, res)



if __name__ == "__main__":
    bot.infinity_polling()
