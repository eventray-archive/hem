# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
import unittest
from hem.text import slugify


class TestSlugify(unittest.TestCase):
    def test_should_always_return_lowercase_words(self):
        self.assertEqual(slugify('ALVAROJUSTEN'), 'alvarojusten')

    def test_should_replace_space_with_dash(self):
        self.assertEqual(slugify('Alvaro Justen'), 'alvaro-justen')

    def test_should_ignore_unecessary_spaces(self):
        self.assertEqual(slugify('  alvaro   justen  '), 'alvaro-justen')

    def test_should_replace_nonascii_chars_with_corresponding_ascii_chars(self):
        self.assertEqual(slugify('áÁàÀãÃâÂäÄ'), 'aaaaaaaaaa')
        self.assertEqual(slugify('éÉèÈẽẼêÊëË'), 'eeeeeeeeee')
        self.assertEqual(slugify('íÍìÌĩĨîÎïÏ'), 'iiiiiiiiii')
        self.assertEqual(slugify('óÓòÒõÕôÔöÖ'), 'oooooooooo')
        self.assertEqual(slugify('úÚùÙũŨûÛüÜ'), 'uuuuuuuuuu')
        self.assertEqual(slugify('ćĆĉĈçÇ'), 'cccccc')

    def test_should_accept_unicode_text(self):
        self.assertEqual(slugify('Álvaro Justen'), 'alvaro-justen')

    def test_should_accept_other_input_encodings(self):
        slugged_text = slugify('Álvaro Justen'.encode('utf16'), 'utf16')
        self.assertEqual(slugged_text, 'alvaro-justen')

    def test_should_accept_only_ascii_letters_and_numbers(self):
        slugged_text = slugify('''qwerty123456"'@#$%*()_+\|<>,.;:/?]~[`{}^ ''')
        self.assertEqual(slugged_text, 'qwerty123456')

    def test_should_accept_only_chars_in_permitted_chars_parameter(self):
        slugged_text = slugify('''0987654321gfdsazxcvb''',
                            permitted_chars='abc123')
        self.assertEqual(slugged_text, '321acb')
