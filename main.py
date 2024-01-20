import os
import telebot
from dotenv_vault import load_dotenv
from mcel import mcelTranslate

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

if __name__ == "__main__":
    bot.infinity_polling()
