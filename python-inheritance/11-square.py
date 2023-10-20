#!/usr/bin/python3
""" module square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ create square inheritance from\
        class Rectangle inheritance from class BaseGeometry"""
    def __init__(self, size):
        """ initialize new square with size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return square description """
        return f"[Square] {self.__size}/{self.__size}"
