#!/usr/bin/env python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception since area is not implemented in base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
