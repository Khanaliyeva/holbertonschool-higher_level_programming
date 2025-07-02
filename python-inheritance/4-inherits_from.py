#!/usr/bin/python3
"""
Module 4-inherits_from
Contains the function inherits_from to check if an object is an instance
of a subclass (direct or indirect) of a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
