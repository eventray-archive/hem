# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)


def get_class_from_config(settings, key):
    if key in settings:
        user_modules = settings.get(key).split('.')
        module = '.'.join(user_modules[:-1])
        klass = user_modules[-1]
        imported_module = __import__(module, fromlist=[klass])
        imported_class = getattr(imported_module, klass)
        return imported_class
    else:
        raise Exception('%s config option was not found' % key)
