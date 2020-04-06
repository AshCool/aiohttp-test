from aiohttp import web
from aiohttp_session import get_session

from random import randint
from time import time

# simple method for handling main page
async def main(request):
    # debug stuff
    print("Main handler")
    session = await get_session(request)
    if session.get('user'):
        if session['user'] == 69:
            return web.Response(text="#{}? Nice.".format(session['user']))
        return web.Response(text="Hello, #{}.".format(session['user']))
    else:
        return web.Response(text="Generic text")

# method that is redirecting
def redirect(request, route):
    url = request.app.router[route].url_for()
    raise web.HTTPFound(url)

# method that is setting the session
def set_session(session, user_id, request):
    # debug stuff
    print("Setting session for user ", user_id)
    session['user'] = str(user_id)
    # session['last_visit'] = time()
    # debug stuff
    print("Redirecting to login once again")
    redirect(request, 'login')

# class for /login view methods
class Login(web.View):
    
    async def get(self):
        # debug stuff
        print("Login GET handler")
        session = await get_session(self.request)
        if session.get('user'):
            # debug stuff
            print("Got user ", session['user'])
            print("Redirecting to main page")
            redirect(self.request, 'main')
        else:
            set_session(session, randint(0, 100), self.request)

        return web.Response(text="Generic text, from a different place")