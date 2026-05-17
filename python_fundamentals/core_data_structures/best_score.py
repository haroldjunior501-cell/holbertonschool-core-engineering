#!/usr/bin/env python3
"""Function to return the key with the biggest integer value."""


def best_score(a_dictionary):
    """Return the key with the highest value, or None if empty/None."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
