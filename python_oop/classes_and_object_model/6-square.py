#!/usr/bin/env python3
"""Module defining a Square class with position and string representation."""


class Square:
    """Represents a square with size, position, and print capability."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square with validated size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position; must be a tuple of 2 non-negative integers."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of the square."""
        if self.__size == 0:
            return ""
        rows = [""] * self.__position[1]
        rows += [" " * self.__position[0] + "#" * self.__size
                 for _ in range(self.__size)]
        return "\n".join(rows)

    def my_print(self):
        """Print the square using # characters with position offset."""
        print(self)
