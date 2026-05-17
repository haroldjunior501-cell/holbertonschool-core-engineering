#!/usr/bin/env python3
"""Function to replace an element in a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace element at idx; return list unchanged if idx is invalid."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
