#!/usr/bin/python3
class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            Exception: Always raises with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')
