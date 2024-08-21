import functools
def check_types(func):
    def wrapper(*args, **kwargs):
        ann = func.__annatations__

    return wrapper

@check_types
def sum(a: int, b: int) -> int:
    return a + b

print(sum(4, 7))
print(sum(4, '7'))