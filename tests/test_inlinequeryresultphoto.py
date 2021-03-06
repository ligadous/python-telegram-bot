#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2016
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains a object that represents Tests for Telegram
InlineQueryResultPhoto"""

import sys

if sys.version_info[0:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest

sys.path.append('.')

import telegram
from tests.base import BaseTest


class InlineQueryResultPhotoTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Telegram InlineQueryResultPhoto."""

    def setUp(self):
        self.id = 'id'
        self.type = 'photo'
        self.photo_url = 'photo url'
        self.photo_width = 10
        self.photo_height = 15
        self.thumb_url = 'thumb url'
        self.title = 'title'
        self.description = 'description'
        self.caption = 'caption'
        self.input_message_content = telegram.InputTextMessageContent('input_message_content')
        self.reply_markup = telegram.InlineKeyboardMarkup([[
            telegram.InlineKeyboardButton('reply_markup')
        ]])

        self.json_dict = {
            'type': self.type,
            'id': self.id,
            'photo_url': self.photo_url,
            'photo_width': self.photo_width,
            'photo_height': self.photo_height,
            'thumb_url': self.thumb_url,
            'title': self.title,
            'description': self.description,
            'caption': self.caption,
            'input_message_content': self.input_message_content.to_dict(),
            'reply_markup': self.reply_markup.to_dict(),
        }

    def test_photo_de_json(self):
        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict)

        self.assertEqual(photo.type, self.type)
        self.assertEqual(photo.id, self.id)
        self.assertEqual(photo.photo_url, self.photo_url)
        self.assertEqual(photo.photo_width, self.photo_width)
        self.assertEqual(photo.photo_height, self.photo_height)
        self.assertEqual(photo.thumb_url, self.thumb_url)
        self.assertEqual(photo.title, self.title)
        self.assertEqual(photo.description, self.description)
        self.assertEqual(photo.caption, self.caption)
        self.assertDictEqual(photo.input_message_content.to_dict(),
                             self.input_message_content.to_dict())
        self.assertDictEqual(photo.reply_markup.to_dict(), self.reply_markup.to_dict())

    def test_photo_to_json(self):
        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict)

        self.assertTrue(self.is_json(photo.to_json()))

    def test_photo_to_dict(self):
        photo = telegram.InlineQueryResultPhoto.de_json(self.json_dict).to_dict()

        self.assertTrue(self.is_dict(photo))
        self.assertDictEqual(self.json_dict, photo)


if __name__ == '__main__':
    unittest.main()
