# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
import unittest


class TestInterfaces(unittest.TestCase):
    def test_dbsession(self):
        """ Shouldn't be able to instantiate the interface """
        from hem.interfaces import IDBSession

        def make_session():
            IDBSession('1')

        self.assertRaises(TypeError, make_session)
