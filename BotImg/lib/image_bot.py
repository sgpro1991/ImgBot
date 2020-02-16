from .image_watermark import ImageWatermark
from telebot import types


class ImageBot(object):
    def __init__(self, message, t_bot):
        self.message = message
        print(message)
        self.types = types
        self.bot = t_bot

    def send_message(self, text, chat_id, reply_markup=None) -> dict:
        c = self.bot.send_message(chat_id,
                                  text,
                                  reply_markup=reply_markup)
        return c

    @staticmethod
    def create_button(text: str, callback_data: str) -> object:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text=text, callback_data=callback_data)
        markup.add(btn)
        return markup

    def send_msg_dialog(self, text, chat_id):
        reply_markup = self.create_button('next', callback_data='get_image')
        self.send_message(text, chat_id, reply_markup)

    def send_msg_dialog_img(self, text, chat_id):
        reply_markup = self.create_button('next', callback_data='get_image')
        img = self.get_image()
        self.bot.send_photo(chat_id, img)
        self.send_message(text, chat_id, reply_markup)

    @staticmethod
    def get_image():
        return ImageWatermark().watermark()
