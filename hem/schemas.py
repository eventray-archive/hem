import colander
import deform

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

        if value != csrf_token:
            raise colander.Invalid(node, 'Bad CSRF token')
    return validate_csrf

class CSRFSchema(colander.Schema):
    csrf = colander.SchemaNode(
        colander.String()
        , default = deferred_csrf_default
        , validator = deferred_csrf_validator
        , widget = deform.widget.HiddenWidget(),
    )
