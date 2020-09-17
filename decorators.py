__author__ = 'Mihail Mihaylov'
import functools


user = {'user_name': 'Jose', 'secure_level': 'admin', 'password': 10000}
user1 = {'user_name': 'Jose', 'secure_level': 'guest', 'password': 123456}


def access_level(level_of_access):
    def secure_func(func):
        @functools.wraps(func)
        def secure(*args, **kwargs):
            if not args:
                if user['secure_level'] == level_of_access:
                    return func(*args, **kwargs)
                else:
                    return 'No admin rights'
            else:
                if args[0]['secure_level'] == level_of_access:
                    return func(*args, **kwargs)
                else:
                    return 'No Rights'
        return secure
    return secure_func


@access_level('admin')
def get_admin_password():
    return user['password']


@access_level('guest')
def get_user_password(my_user):
    return my_user['password']

