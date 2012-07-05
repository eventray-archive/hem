from hem.interfaces import IDBSession

def get_session(request):
    session = request.registry.getUtility(IDBSession)

    return session


