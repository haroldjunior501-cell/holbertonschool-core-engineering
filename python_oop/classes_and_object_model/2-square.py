#!/usr/bin/env python3
"""Module defining a Square class with validated private size attribute."""


class Square:
    """Represents a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize Square with a validated size (default 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
