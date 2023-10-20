#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file and
returns the number of characters added"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str): name of file. Defaults to "".
        text (str): text we want to add. Defaults to "".

    Return: number of characters added
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
