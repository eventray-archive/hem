from hem.interfaces import IDBSession

def get_session(request):
    if request.registry.queryUtility(IDBSession):
        session = request.registry.getUtility(IDBSession)

        return session
    else:
        raise Exception(
            'You need to register a DBSession to IDBSession interface'
        )


