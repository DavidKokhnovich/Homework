import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция ‘{func.__name__}’ начала выполнение в {start_time} и завершила в {end_time}")
        return result
    return wrapper

@log_time
def my_function():
    time.sleep(2)
print('Функция выполняется...')

my_function()