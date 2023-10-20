#!/usr/bin/python3
""" class Rectangle that inherits from imported class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle
    width is private
    height is private"""
    def __init__(self, width, height):
        """ initialize new rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
