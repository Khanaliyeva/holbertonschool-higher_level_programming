#!/usr/bin/python3
"""
Module 4-inherits_from
Contains the function inherits_from that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass of a_class (not a_class itself)."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
