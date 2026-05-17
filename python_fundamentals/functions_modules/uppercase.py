#!/usr/bin/env python3
"""Function to print a string in uppercase using ASCII conversion."""


def uppercase(str):
    """Print str in uppercase followed by a new line."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
