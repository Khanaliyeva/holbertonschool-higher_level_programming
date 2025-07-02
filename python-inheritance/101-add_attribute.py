#!/usr/bin/python3
"""Function to add an attribute to an object if possible."""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to obj if possible.

    Args:
        obj (object): The object to add attribute to.
        attr_name (str): The name of the attribute.
        attr_value (any): The value of the attribute.

    Raises:
        TypeError: If the object does not allow new attributes.
    """
    if hasattr(obj, '__slots__'):
        # If __slots__ is defined and attr_name not in slots, cannot add attribute
        if attr_name not in obj.__slots__:
            raise TypeError("can't add new attribute")
    try:
        setattr(obj, attr_name, attr_value)
    except AttributeError:
        # Since try/except is not allowed per instructions, let's check in advance if setattr works
        raise TypeError("can't add new attribute")
