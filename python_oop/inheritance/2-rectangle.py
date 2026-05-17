#!/usr/bin/env python3
"""Module defining Rectangle with area and string representation."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with area and readable string output."""

    def __init__(self, width, height):
        """Initialize with validated private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation: [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
