#!/usr/bin/python3
"""
This module contains a function is_kind_of_class to check if an object
is an instance of, or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherited
    from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited
        from a_class; otherwise False.
    """
    return isinstance(obj, a_class)
