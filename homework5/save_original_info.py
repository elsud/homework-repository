"""
Module with decorator which saves name and documentation of the
original function. Also it saves original function in attribute
__original_func of new decorated function.
So decorated function print result before returning it
and original function return result without printing.
"""
import functools


def save_info(func):
    """Function-wrapper for wrapper which save information about original function
    and add attribute with link to original function."""

    def inner(decorator):
        decorator.__doc__ = func.__doc__
        decorator.__name__ = func.__name__
        decorator.__original_func = func
        return decorator

    return inner


def print_result(func):
    @save_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
