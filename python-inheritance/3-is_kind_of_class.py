#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains the function is_kind_of_class to check if an object is an instance
of a class or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass, else False."""
    return isinstance(obj, a_class)
