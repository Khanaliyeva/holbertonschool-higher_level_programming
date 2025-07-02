#!/usr/bin/python3
"""Defines MyInt class that inherits from int and inverts == and != operators."""


class MyInt(int):
    """MyInt class that rebels by inverting == and !=."""

    def __eq__(self, other):
        """Invert the == operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return not super().__ne__(other)
