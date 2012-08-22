# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
import unittest
from hem.text import slugify


class TestSlugify(unittest.TestCase):
    def test_should_always_return_lowercase_words(self):
        self.assertEquals(slugify('ALVAROJUSTEN'), 'alvarojusten')

    def test_should_replace_space_with_dash(self):
        self.assertEquals(slugify('Alvaro Justen'), 'alvaro-justen')

    def test_should_ignore_unecessary_spaces(self):
        self.assertEquals(slugify('  alvaro   justen  '), 'alvaro-justen')

    def test_should_replace_nonascii_chars_with_corresponding_ascii_chars(self):
        self.assertEquals(slugify('áÁàÀãÃâÂäÄ'.decode('utf8')), 'aaaaaaaaaa')
        self.assertEquals(slugify('éÉèÈẽẼêÊëË'.decode('utf8')), 'eeeeeeeeee')
        self.assertEquals(slugify('íÍìÌĩĨîÎïÏ'.decode('utf8')), 'iiiiiiiiii')
        self.assertEquals(slugify('óÓòÒõÕôÔöÖ'.decode('utf8')), 'oooooooooo')
        self.assertEquals(slugify('úÚùÙũŨûÛüÜ'.decode('utf8')), 'uuuuuuuuuu')
        self.assertEquals(slugify('ćĆĉĈçÇ'.decode('utf8')), 'cccccc')

    def test_should_accept_unicode_text(self):
        self.assertEquals(slugify(u'Álvaro Justen'), 'alvaro-justen')

    def test_should_accept_other_input_encodings(self):
        slugged_text = slugify(u'Álvaro Justen'.encode('utf16'), 'utf16')
        self.assertEquals(slugged_text, 'alvaro-justen')

    def test_should_accept_only_ascii_letters_and_numbers(self):
        slugged_text = slugify('''qwerty123456"'@#$%*()_+\|<>,.;:/?]~[`{}^ ''')
        self.assertEquals(slugged_text, 'qwerty123456')

    def test_should_accept_only_chars_in_permitted_chars_parameter(self):
        slugged_text = slugify('''0987654321gfdsazxcvb''',
                            permitted_chars='abc123')
        self.assertEquals(slugged_text, '321acb')
