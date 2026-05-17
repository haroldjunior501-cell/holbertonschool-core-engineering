#!/usr/bin/env python3
"""Function to replace or add a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Update or insert key with value in a_dictionary and return it."""
    a_dictionary[key] = value
    return a_dictionary
