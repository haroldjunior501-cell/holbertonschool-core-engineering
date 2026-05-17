#!/usr/bin/env python3
"""Function to compute a raised to the power of b."""


def pow(a, b):
    """Return a raised to the power of b."""
    result = 1
    for _ in range(b):
        result *= a
    return result
