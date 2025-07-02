#!/usr/bin/python3
"""
Module 7-base_geometry
Defines class BaseGeometry with methods area and integer_validator.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable (used for error messages).
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer or is a bool.
            ValueError: If value <= 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
