#!/usr/bin/env python3
"""Appends a string to a text file and returns characters added."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
