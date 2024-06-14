#!/usr/bin/python3
class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            NotImplementedError: Always raises with the 
            message 'area() is not implemented'.
        """
        raise NotImplementedError("area() is not implemented")

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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        Returns:
            str: String representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square with size.
        Args:
            size (int): Size of the square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the Square.
        Returns:
            str: String representation of the Square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
