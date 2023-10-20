#!/usr/bin/python3
"""Write a function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """fct that returns the JSON representation of an object

    Args:
        my_obj (_type_): _description_

    Return: JSON representation of an object
    """
    return json.dumps(my_obj)
