#!/usr/bin/env python3
"""Function to safely print integer elements from the first x of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers in my_list[:x], skip non-integers, return count."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
