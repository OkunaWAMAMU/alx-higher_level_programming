#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that
        inherited from a_class, False otherwise.
    """
    # Get the object's class using type()
    obj_class = type(obj)

    """
    Check if the object's class is not the
    specified class and is a subclass of it
    """
    return issubclass(obj_class, a_class) and obj_class != a_class
