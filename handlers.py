from aiohttp import web
from aiohttp_session import get_session
import aiohttp_jinja2
from aiomysql.sa.engine import Engine
from pymysql.err import ProgrammingError

async def db_request(db, expression):
    # getting connection from the engine's connection pool
    try:
        connection = await db.acquire()
    except AttributeError:
        print('Engine object was not passed')
        return []

    # executing SQL statement via connection
    try:
        wrapped_result = await connection.execute(expression)
    except ProgrammingError:
        print('Incorrect SQL syntax')
        await connection.close()
        return []

    # result is some wrap, unwrap it
    result = await wrapped_result.fetchall()

    # some wraps again, getting all rows from the result, then coverting them to tuple (from ValueView) and printing
    data = []
    for res in result:
        data.append(list(res.values()))
    # closing the connection
    await connection.close()

    return data

# method that is redirecting
def redirect(request, route):
    url = request.app.router[route].url_for()
    raise web.HTTPFound(url)

# method that is setting the session
def set_session(session, user_login, request):
    # debug stuff
    print("Setting session for user", user_login)
    session['user_login'] = user_login
    # debug stuff
    print("Redirecting to main page")
    redirect(request, 'index')

# class for / view methods
class Index(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        # debug stuff
        print("Main get handler")
        session = await get_session(self.request)
        print(session['user_login'])

        '''# getting connection from the engine's connection pool
        connection = await self.request.app['db'].acquire()
        print(type(self.request.app['db']))
        # executing SQL statement via connection
        print('SELECT * FROM user_data WHERE login = \'' + session['user_login'] + '\';')
        result = await connection.execute('SELECT * FROM user_data WHERE login = \'' + session['user_login'] + '\';')
        # result is some wrap, unwrap it
        result_result = await result.fetchall()
        # some wraps again, getting all rows from the result, then coverting them to tuple (from ValueView) and printing
        data = []
        for res in result_result:
            data.append(list(res.values()))
            print(list(res.values()))
        # closing the connection
        await connection.close()'''

        data = await db_request(self.request.app['db'],
                          'SELECT * FROM user_data WHERE login = \'' + session['user_login'] + '\';')

        return {'session': session['user_login'], 'data': data}

    async def post(self):
        print("Main post handler")
        data = await self.request.post()
        session = await get_session(self.request)

        # logout button pressed
        if data['action'] == 'logout':
            # clearing current session and redirecting to login page
            session.clear()
            redirect(self.request, 'login')


# class for /login view methods
class Login(web.View):

    @aiohttp_jinja2.template('login.html')
    async def get(self):
        # debug stuff
        print("Login GET handler")
        session = await get_session(self.request)
        if session.get('user'):
            # debug stuff
            print("Got user ", session['user'])
            print("Redirecting to main page")
            redirect(self.request, '/')
        return {'content': 'Please enter your login and password'}

    async def post(self):
        print("Login POST handler")
        data = await self.request.post()



        session = await get_session(self.request)
        set_session(session, data['login'], self.request)

class Signin(web.View):

    @aiohttp_jinja2.template('signin.html')
    async def get(self):
        # debug stuff
        print("Signin GET handler")
        session = await get_session(self.request)

        return {'content': 'Create new account by entering your new login and password'}