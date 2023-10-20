#!/usr/bin/python3
""" class Rectangle that inherits from imported class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle
    width is private
    height is private
    area : return area of rectangle
    """
    def __init__(self, width, height):
        """ initialize new rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return rectangle description """
        return f"[Rectangle] {self.__width}/{self.__height}"
