# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
    unicode_literals)
import colander
import deform
import six


@colander.deferred
def deferred_csrf_default(node, kw):
    request = kw.get('request')
    csrf_token = request.session.get_csrf_token()
    return csrf_token


@colander.deferred
def deferred_csrf_validator(node, kw):
    def validate_csrf(node, value):
        request = kw.get('request')
        csrf_token = request.session.get_csrf_token()

        if six.PY3:
            if not isinstance(csrf_token, str):
                csrf_token = csrf_token.decode('utf-8')

        if value != csrf_token:
            raise colander.Invalid(node,
                                   'Invalid cross-site scripting token')
    return validate_csrf


class CSRFSchema(colander.Schema):
    csrf_token = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.HiddenWidget(),
        default=deferred_csrf_default,
        validator=deferred_csrf_validator,
    )
