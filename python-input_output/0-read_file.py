#!/usr/bin/python3
"""Defines a function to read and print a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
