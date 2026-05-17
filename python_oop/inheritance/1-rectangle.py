#!/usr/bin/env python3
"""Module defining Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated private width and height."""

    def __init__(self, width, height):
        """Initialize with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
