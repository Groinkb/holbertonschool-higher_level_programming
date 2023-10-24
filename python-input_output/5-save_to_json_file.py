#!/usr/bin/python3
"""return json repr"""
import json


def save_to_json_file(my_obj, filename):
    """return json repr"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
