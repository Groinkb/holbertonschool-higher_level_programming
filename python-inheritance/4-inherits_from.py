#!/usr/bin/python3
"""tells if object is in the same class"""


def inherits_from(obj, a_class):
    """tells if object is in the same class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
