#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The rectangle's width (default is 0).
            height (int): The rectangle's height (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
