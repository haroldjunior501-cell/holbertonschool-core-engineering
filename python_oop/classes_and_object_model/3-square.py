#!/usr/bin/env python3
"""Module defining a Square class with area method."""


class Square:
    """Represents a square with size validation and area computation."""

    def __init__(self, size=0):
        """Initialize Square with a validated size (default 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
