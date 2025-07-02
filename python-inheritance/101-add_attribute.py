#!/usr/bin/python3
"""Function that adds a new attribute to an object if possible."""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to obj if possible.

    Args:
        obj (object): The object to add attribute to.
        attr_name (str): The attribute name.
        attr_value (any): The attribute value.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        # If no __dict__, maybe __slots__ defines allowed attributes
        if not hasattr(obj, '__slots__'):
            raise TypeError("can't add new attribute")
        else:
            slots = obj.__slots__
            if isinstance(slots, str):
                slots = (slots,)
            if attr_name not in slots:
                raise TypeError("can't add new attribute")

    # If no exception raised, add the attribute
    object.__setattr__(obj, attr_name, attr_value)
