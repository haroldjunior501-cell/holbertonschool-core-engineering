#!/usr/bin/env python3
"""Function to safely divide two integers, always printing the result."""


def safe_print_division(a, b):
    """Divide a by b; print result in finally block; return result or None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
