# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
from mock       import Mock
from pyramid    import testing
import unittest


class TestLib(unittest.TestCase):
    def test_get_session(self):
        from hem.interfaces import IDBSession
        from hem.db import get_session
        request = testing.DummyRequest()
        request.registry = Mock()

        session = Mock()

        getUtility = Mock()
        getUtility.return_value = session

        request.registry.getUtility = getUtility

        new_session = get_session(request)

        getUtility.assert_called_with(IDBSession)
        assert new_session == session
