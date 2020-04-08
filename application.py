from aiohttp import web

import jinja2
import aiohttp_jinja2

from aiohttp_session import session_middleware, SimpleCookieStorage

from routes import routes
from middlewares import authorize
from database_handlers import init_mysql_db, close_mysql_db

async def on_shutdown(app):
    close_mysql_db(app)
    print("shutting down")

# list of middlewares
_middlewares = [
    session_middleware(SimpleCookieStorage()), # no security
    authorize
]
# initializing app, appending middlewares
app = web.Application(middlewares=_middlewares)

# appending templates
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# adding routes from routes.py to route table
for route in routes:

    app.router.add_route(route[0], route[1], route[2], name=route[3])
app.add_routes([web.static('/static', 'static')])

# adding signals
app.on_startup.append(init_mysql_db)
app.on_cleanup.append(on_shutdown)

print("The app is running")
web.run_app(app)
print("The app stopped running")