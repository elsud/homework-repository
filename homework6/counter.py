"""Module with class decorator instanse_counter which add to the class
2 methods:
get_created_instances - returns counter of all created instances,
reset_instances_counter - resets counter and returns count of instances before reset.
"""
import functools


def instances_counter(cls):
    """Class decorator, which adds 2 methods to class: count of all
    creating instances and reset this counter."""

    counter = 0
    original_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        """Adding to __init__ increase of a counter."""
        nonlocal counter
        counter += 1
        original_init(self, *args, **kwargs)

    @staticmethod
    def get_created_instances():
        """Giving counter of all created instances of decorated class."""
        return counter

    @staticmethod
    def reset_instances_counter():
        """Reset counter of all created instances of decorated class.
        I wasn't sure about deleting of all instances too, but as we haven't any mention
        about this deleting I decided to reset counter only."""
        nonlocal counter
        previous, counter = counter, 0
        return previous

    cls.__init__ = new_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls
