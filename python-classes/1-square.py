#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if size < 0:
            print("Size must be >= 0")
            # You can raise an exception here if you want to handle it differently
            # For example, raise ValueError("Size must be >= 0")
        else:
            self.__size = size

# Usage
my_square = Square(5)
print(my_square.__dict__.get('_Square__size', 'Invalid size'))  # Accessing private attribute
