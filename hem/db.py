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
        raise Exception('no IDBSession registered')

    # Doing this since scoped session is callable
    # but we don't want to have sqlalchemy as a
    # dependency of hem
    is_scoped_session = hasattr(session, 'query')

    if callable(session) and not is_scoped_session:
        return session(request)
    else:
        return session
