from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session

@middleware
async def authorize(request, handler):
    #debug stuff
    print("authorize handler from ", request)

    # kinda self-explanatory?
    def trying_to_log_in(path):
        for r in ['/login']:
            if path.startswith(r):
                return True
        return False
    
    session = await get_session(request)

    # if user is already logged in, let them do their things
    if session.get('user'):
        return await handler(request)

    # if user is not logged in and not even trying to...
    elif not trying_to_log_in(request.path):
        # ...step them in the right direction
        url = request.app.router['login'].url_for()
        raise web.HTTPFound(url)
        return handler(request)

    # if user is not logged in, but is trying to
    else:
        return await handler(request)