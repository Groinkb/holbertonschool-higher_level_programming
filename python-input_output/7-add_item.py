#!/usr/bin/python3
"""function that load list from file then add args in list and save it"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        new_list = load_from_json_file("add_item.json")
    except:
        new_list = []
    for i in range(1, len(argv)):
        new_list.append(argv[i])
    save_to_json_file(new_list, "add_item.json")
