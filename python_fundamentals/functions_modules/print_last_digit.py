#!/usr/bin/env python3
"""Function to print and return the last digit of a number."""


def print_last_digit(number):
    """Print and return the last digit of number (always positive)."""
    last = abs(number) % 10
    print("{}".format(last), end='')
    return last
