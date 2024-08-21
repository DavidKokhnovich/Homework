from time import sleep
def optimaze(func):
    counter, cache = 0, dict()
    def wrap(x):
        nonlocal counter
        counter += 1
        if counter in range(1, 4) and cache:
            return cache['cache']
        cache['cache'], counter = func(x), 0
        return cache['cache']
    return wrap
@optimaze
def my_function(x):
    sleep(2)
    return x * x

print(my_function(7))
print(my_function(3))
print(my_function(4))
print(my_function(5))
print(my_function(1))
print(my_function(9))
print(my_function(11))
