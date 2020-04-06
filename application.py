import asyncio
from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from cryptography import fernet
import base64

from routes import routes
from middlewares import *

# TODO: the security
fernet_key = fernet.Fernet.generate_key()
print(fernet_key)
secret_key = base64.urlsafe_b64decode(fernet_key)
print(secret_key)

# list of middlewares
_middlewares = [
    session_middleware(EncryptedCookieStorage(secret_key)),
    authorize
]

app = web.Application(middlewares=_middlewares)

# adding routes from routes.py to route table
for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

print("The app is running")
web.run_app(app)
print("The app stopped running")