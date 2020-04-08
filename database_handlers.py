import sqlalchemy as sa
from aiomysql.sa import create_engine

async def init_mysql_db(app):
    engine = await create_engine(
        host="127.0.0.1",
        db="main_db",
        user="root",
        password="1234",
        minsize=1,
        maxsize=10
    )
    app['db'] = engine
    print("engine initialized")

async def close_mysql_db(app):
    app['db'].close()
    await app['db'].wait_closed()
    print("closing db connection")