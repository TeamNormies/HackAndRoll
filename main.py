import os
import telebot
from dotenv_vault import load_dotenv
from mcel import mcelTranslate
from uwu import english_to_uwu
from owo import english_to_owo

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

@bot.message_handler(commands=['owo', 'OwO'])
def owoify_message(message):
    text = "Enter text to OwOify!"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, translate_owo)

@bot.message_handler(commands=['uwu'])
def uwuify_message(message):
    bot.send_message(message.chat.id, "uwuify youw message!")
    bot.register_next_step_handler(message, translate_uwu)

def translate_owo(message): 
    output = english_to_owo(message.text) 
    bot.send_message(message.chat.id, output)

def modifyMCEL(message):
    output = mcelTranslate(message.text)
    bot.send_message(message.chat.id, output)

def translate_uwu(message):
    res = english_to_uwu(message.text)
    bot.send_message(message.chat.id, res)

if __name__ == "__main__":
    bot.infinity_polling()
