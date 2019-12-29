#!/usr/bin/env python3
from functools import wraps


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


def my_logger(original_function):
    import logging
    logging.basicConfig(
        filename=f"{original_function.__name__}.log", level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args:{args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper


def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec(s)")
        return result
    return wrapper

# @decorator_function
@decorator_class
def display():
    print('display function ran')


# @decorator_function
# @decorator_class
@my_timer
@my_logger
def display_info(name, age):
    print(f"display info ran with arguments ({name},{age})")


display()
display_info('Pablo', 25)
