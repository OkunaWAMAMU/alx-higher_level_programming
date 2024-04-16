#!/usr/bin/python3

def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    # Get all attributes and methods of the object
    attributes_and_methods = dir(obj)

    # Filter out private attributes and methods
    filtered_attributes_and_methods = [
        item for item in attributes_and_methods if not item.startswith('__')
    ]

    return filtered_attributes_and_methods
