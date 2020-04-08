from handlers import Index, Login, Signin

routes = [
    ('*', '/', Index, 'index'),
    ('*', '/login', Login, 'login'),
    ('*', '/signin', Signin, 'signin')
]