#!/usr/bin/python3
"""Defines a function that appends text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file and return the number
    of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
