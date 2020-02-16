from config import BOT_TOKEN, PROXY
from .image_bot import ImageBot
import telebot
from telebot import apihelper

apihelper.proxy = PROXY
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message: telebot):
    ImageBot(message, bot).send_msg_dialog('Привет, ты написал мне /start', message.chat.id)


@bot.callback_query_handler(lambda query: query.data == "get_image")
def get_image(message):
    ImageBot(message, bot).send_msg_dialog_img('Привет', message.from_user.id)
