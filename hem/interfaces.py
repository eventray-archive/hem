# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
from zope.interface import Interface


class IDBSession(Interface):
    """ Marker interface for registering a db session
    """
    pass
