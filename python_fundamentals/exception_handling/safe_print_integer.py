#!/usr/bin/env python3
"""Function to safely print an integer."""


def safe_print_integer(value):
    """Print value as integer and return True; return False if not int."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
