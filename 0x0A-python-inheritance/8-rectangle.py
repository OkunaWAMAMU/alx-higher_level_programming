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

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
