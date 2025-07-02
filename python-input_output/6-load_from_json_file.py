#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The file containing JSON data.

    Returns:
        object: The Python object deserialized from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
