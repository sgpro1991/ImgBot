from lib.flickr import FlackrImage
from lib.image_bot import ImageBot
import unittest
import telebot
from config import BOT_TOKEN, PROXY
from telebot import apihelper


class FlackrTest(unittest.TestCase):
    def setUp(self) -> None:
        self.flickr = FlackrImage()

    def test_search_img(self):
        c = self.flickr.search_img('cat')
        self.assertTrue(isinstance(c, dict))
        self.assertEqual(c['photos']['page'], 1)

    def test_get_random_image(self):
        c = self.flickr.get_random_image('cat')
        self.assertTrue(isinstance(c, dict))


class ImageBotTest(unittest.TestCase):
    def setUp(self) -> None:
        bot = telebot.TeleBot(BOT_TOKEN)
        apihelper.proxy = PROXY
        message = {'content_type': 'text', 'message_id': 240,
                   'from_user': {'id': 146529206, 'is_bot': False, 'first_name': 'Sgpro1991', 'username': None,
                                 'last_name': 'Sergo', 'language_code': 'ru'}, 'date': 1581875490,
                   'chat': {'type': 'private', 'last_name': 'Sergo', 'first_name': 'Sgpro1991', 'username': None,
                            'id': 146529206, 'title': None, 'all_members_are_administrators': None, 'photo': None,
                            'description': None, 'invite_link': None, 'pinned_message': None, 'sticker_set_name': None,
                            'can_set_sticker_set': None}, 'forward_from_chat': None, 'forward_from_message_id': None,
                   'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None,
                   'media_group_id': None, 'author_signature': None, 'text': '/start', 'entities': '',
                   'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None,
                   'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None,
                   'venue': None, 'animation': None, 'new_chat_member': None, 'new_chat_members': None,
                   'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None,
                   'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None,
                   'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None,
                   'successful_payment': None, 'connected_website': None, 'json': {'message_id': 240,
                                                                                   'from': {'id': 146529206,
                                                                                            'is_bot': False,
                                                                                            'first_name': 'Sgpro1991',
                                                                                            'last_name': 'Sergo',
                                                                                            'language_code': 'ru'},
                                                                                   'chat': {'id': 146529206,
                                                                                            'first_name': 'Sgpro1991',
                                                                                            'last_name': 'Sergo',
                                                                                            'type': 'private'},
                                                                                   'date': 1581875490, 'text': '/start',
                                                                                   'entities': [
                                                                                       {'offset': 0, 'length': 6,
                                                                                        'type': 'bot_command'}]}}
        self.image_bot = ImageBot(message, bot)

    def test_send_message(self):
        c = self.image_bot.send_message('111', 146529206, )
        self.assertEqual(c.content_type, 'text')
