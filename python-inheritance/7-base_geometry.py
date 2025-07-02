#!/usr/bin/python3
"""
Module 7-base_geometry
Defines class BaseGeometry with area() and integer_validator() methods.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
        - name: string representing the name of the parameter
        - value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
