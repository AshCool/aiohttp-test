from aiohttp import web
from aiohttp_session import get_session
import aiohttp_jinja2

async def db_request(db, expression):

    print("got request " + expression)
    # getting connection from the engine's connection pool
    try:
        wrapped_connection = await db.acquire()
    except AttributeError:
        print('Engine object was not passed')
        return [[False]]

    # unwrap the connection
    connection = wrapped_connection.connection
    # execute expression and commit it
    cursor = await connection.cursor()
    await cursor.execute(expression)
    await connection.commit()
    await wrapped_connection.close()

    # fetching results
    result = await cursor.fetchall()
    print(result)
    return result

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

        data = await db_request(self.request.app['db'],
                          'SELECT * FROM user_data WHERE login = \'' + session['user_login'] + '\';')

        return {'user': session['user_login'], 'data': data}

    async def post(self):
        print("Main POST handler")
        data = await self.request.post()
        session = await get_session(self.request)

        # add new link button pressed
        if data['action'] == 'add_link':
            await db_request(self.request.app['db'],
                             'insert into user_data (login, link) '
                             'values(\'' + session['user_login'] + '\', \'' + data['link'] + '\');')
            redirect(self.request, 'index')
        # download link button pressed
        elif data['action'] == 'download':
            pass
        # delete link button pressed
        elif data['action'] == 'delete_link':
            await db_request(self.request.app['db'],
                             'delete from user_data where id = \'' + data['item_id'] + '\';')
            redirect(self.request, 'index')
        # logout button pressed
        elif data['action'] == 'logout':
            # clearing current session and redirecting to login page
            session.clear()
            redirect(self.request, 'login')
        # change password button pressed
        elif data['action'] == 'change':
            redirect(self.request, 'passwordchange')
        # delete account button pressed
        elif data['action'] == 'delete_account':
            await db_request(self.request.app['db'],
                             'delete from user_info where login = \''+ session['user_login'] + '\';')
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
        # getting login/password from the page
        data = await self.request.post()
        # checking for user w/ acquired credentials in DB
        user_exists = await db_request(self.request.app['db'],
                   'select exists(select * from user_info '
                   'where login = \'' + data['login'] + '\' and password = \'' + data['password'] + '\');')
        # if user is found
        print("???")
        if user_exists[0][0]:
            # logging in
            print('Logging in')
            session = await get_session(self.request)
            set_session(session, data['login'], self.request)
        else:
            # else - showing error message
            print('Incorrect login and/or password')
            return web.Response(body='error')

# class for /signin view methods
class Signin(web.View):

    @aiohttp_jinja2.template('signin.html')
    async def get(self):
        # debug stuff
        print("Signin GET handler")

        return {'content': 'Create new account by entering your new login and password'}

    async def post(self):
        print('Signin POST handler')
        # getting login/password from the page
        data = await self.request.post()
        # checking for user w/ same login in DB
        user_exists = await db_request(self.request.app['db'],
                                       'select exists(select * from user_info '
                                       'where login = \'' + data['login'] + '\');')
        # if user is found
        if user_exists[0][0]:
            # showing error message
            print('User already exists')
            return web.Response(body='error')
        else:
            # adding new user to the DB
            print('adding ' + data['login'] + data['password'])
            await db_request(self.request.app['db'],
                                       'insert into user_info (login, password) '
                                       'values(\'' + data['login'] + '\', \'' + data['password'] + '\');')
            # logging in
            print('Logging in')
            session = await get_session(self.request)
            set_session(session, data['login'], self.request)

# class for /passwordchange view methods
class PasswordChange(web.View):

    @aiohttp_jinja2.template('passwordchange.html')
    async def get(self):
        print("Passwordchange GET handler")
        session = await get_session(self.request)
        return {'content': 'Please, enter your new password, ' + session['user_login']}

    async def post(self):
        print("Passwordchange POST handler")
        # getting new password from page
        data = await self.request.post()
        # getting user's login via session
        session = await get_session(self.request)
        # updating password
        await db_request(self.request.app['db'],
                         'update user_info set password = \'' + data['new_password'] +
                         '\' where login = \'' + session['user_login'] + '\';')

        redirect(self.request, 'index')
