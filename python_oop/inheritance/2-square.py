#!/usr/bin/env python3
"""Module defining Square with its own string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with a square-specific string representation."""

    def __init__(self, size):
        """Initialize Square with validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation: [Square] size/size."""
        return "[Square] {}/{}".format(self.__size, self.__size)
