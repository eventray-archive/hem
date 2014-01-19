# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from hem.interfaces import IDBSession


def get_session(request):
    if hasattr(request, 'db_session'):
        return request.db_session
    elif request.registry.queryUtility(IDBSession):
        session = request.registry.getUtility(IDBSession)
    else:
        raise Exception(
            'You need to register a DBSession to IDBSession interface for'
            'horus'
        )

    if callable(session):
        return session(request)
    else:
        return session
