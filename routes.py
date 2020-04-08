from handlers import Index, Login, Signin, PasswordChange

routes = [
    ('*', '/', Index, 'index'),
    ('*', '/login', Login, 'login'),
    ('*', '/signin', Signin, 'signin'),
    ('*', '/passwordchange', PasswordChange, 'passwordchange')
]