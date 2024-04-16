def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        bool: True if the object is an instance of a class that inherited
              (directly or indirectly) from the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class)
