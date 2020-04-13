from json import load
from aiomysql.sa import create_engine

CONFIG_FILE = 'db_settings.json'

async def init_mysql_db(app):
    with open(CONFIG_FILE) as config:
        settings = load(config)

    engine = await create_engine(
        host=settings['host'],
        port=settings['port'],
        db=settings['db'],
        user=settings['user'],
        password=settings['password'],
        minsize=settings['connection_pool_minsize'],
        maxsize=settings['connection_pool_maxsize']
    )
    app['db'] = engine
    print("engine initialized")

async def close_mysql_db(app):
    app['db'].close()
    await app['db'].wait_closed()
    print("closing db connection")