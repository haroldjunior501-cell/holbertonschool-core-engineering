#!/usr/bin/env python3
"""Module defining Square that inherits from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square as a specialized rectangle."""

    def __init__(self, size):
        """Initialize Square with validated private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
