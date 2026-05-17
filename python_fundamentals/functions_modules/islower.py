#!/usr/bin/env python3
"""Function to check if a character is a lowercase letter."""


def islower(c):
    """Return True if c is lowercase, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')
