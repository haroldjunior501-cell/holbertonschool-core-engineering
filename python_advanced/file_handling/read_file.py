#!/usr/bin/env python3
"""Reads a UTF-8 text file and prints it to stdout."""


def read_file(filename=""):
    """Print the contents of a file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
