#!/usr/bin/python3
"""Module that defines a subclass MyList of list."""


class MyList(list):
    """A subclass of list that can print its elements sorted."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
