def access_control(user_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_type == 'admin':
                return func(*args, **kwargs)
            else:
                return 'denied'
        return wrapper
    return decorator

@access_control('user')
def example_function():
    return 'access'

print(example_function())