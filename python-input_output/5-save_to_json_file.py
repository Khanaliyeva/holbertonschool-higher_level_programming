#!/usr/bin/python3
"""Defines a function that writes an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to serialize.
        filename (str): The filename to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
