#!/usr/bin/python3
"""function that reads obj from file"""
import json


def load_from_json_file(filename):
    """function that reads obj from file"""
    with open(filename, 'r') as file:
        return json.loads(file.read())
