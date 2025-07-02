#!/usr/bin/python3
"""
Module that contains the function class_to_json which returns
the dictionary description with simple data structures
for JSON serialization of an object.
"""

def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj (object): Instance of a class.
    Returns:
        dict: Dictionary of all attributes of obj.
    """
    return obj.__dict__.copy()
