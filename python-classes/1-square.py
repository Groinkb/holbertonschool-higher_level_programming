#!/usr/bin/python3

class Square:
    """A class to represent a square."""

    def __init__(self, size):
        """Initialize the Square object with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size

# Example usage
square = Square(5)
print(square.__dict__.get('_Square__size'))  # Accessing private attribute
