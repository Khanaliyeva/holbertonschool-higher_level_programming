#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj (any): The object to serialize.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
