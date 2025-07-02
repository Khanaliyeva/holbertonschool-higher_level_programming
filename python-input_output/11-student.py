#!/usr/bin/python3
"""Student class module."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in attrs are included.
        Otherwise, all attributes are included.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with those in json.

        Args:
            json (dict): Dictionary with attributes to update.
        """
        for key, value in json.items():
            setattr(self, key, value)
