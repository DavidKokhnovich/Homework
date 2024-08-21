import time
def delay_decorator(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay_decorator(2)
def hello(name):
    print(f'Hello, {name}')

hello('Nikita')