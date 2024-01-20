import os
import telebot
from dotenv_vault import load_dotenv
from mcel import mcel_translate
from nyan import nyan_translate
from uwu import english_to_uwu
from owo import english_to_owo

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
	markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
	btn1 = telebot.types.KeyboardButton("/UwU")
	btn2 = telebot.types.KeyboardButton("/OwO")
	btn3 = telebot.types.KeyboardButton("/Nyan")
	btn4 = telebot.types.KeyboardButton("/MCEL")
	btn5 = telebot.types.KeyboardButton("/Japanese")
	markup.add(btn1,btn2,btn3)
	markup.add(btn4,btn5)
	bot.send_message(chat_id=message.chat.id, text="What do you want to do today?", reply_markup=markup)

@bot.message_handler(commands=["MCEL"])
def toggle_mcel(message):
    bot.send_message(message.chat.id, "Say something!")
    bot.register_next_step_handler(message, modify_mcel)

@bot.message_handler(commands=["Nyan"])
def toggle_nyan(message):
    bot.send_message(message.chat.id, "Say something!")
    bot.register_next_step_handler(message, modify_nyan)

@bot.message_handler(commands=["OwO"])
def owoify_message(message):
    text = "Enter text to OwOify!"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, translate_owo)

@bot.message_handler(commands=['UwU'])
def uwuify_message(message):
    bot.send_message(message.chat.id, "uwuify youw message!")
    bot.register_next_step_handler(message, translate_uwu)

@bot.message_handler(commands=['back'])
def handle_back(message):
    handle_start(message)

def translate_owo(message): 
    output = english_to_owo(message.text) 
    bot.send_message(message.chat.id, output)

def modify_mcel(message):
    output = mcel_translate(message.text)
    bot.send_message(message.chat.id, output)

def translate_uwu(message):
    res = english_to_uwu(message.text)
    bot.send_message(message.chat.id, res)

def modify_nyan(message):
    output = nyan_translate(message.text)
    bot.send_message(message.chat.id, output)

if __name__ == "__main__":
    bot.infinity_polling()
