#!/usr/bin/python3
"""Write a function that writes a string to a text file and
returns the number of characters written"""


def write_file(filename="", text=""):
    """fct that writes a string

    Args:
        filename (str): name of the file. Defaults to "".
        text (str): text we want to write. Defaults to "".

    Return:
        int: number of character wrote in hte file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
