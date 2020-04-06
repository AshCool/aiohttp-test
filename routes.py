from handlers import main, Login

routes = [
    ('GET', '/', main, 'main'),
    ('GET', '/login', Login, 'login')
]