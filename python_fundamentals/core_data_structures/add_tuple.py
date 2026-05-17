#!/usr/bin/env python3
"""Function to add two tuples element-wise, returning a 2-element tuple."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple of 2 integers: sum of first two elements of each."""
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
