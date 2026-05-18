#!/usr/bin/env python3
"""Module defining VerboseList, a list subclass with operation logging."""


class VerboseList(list):
    """A list that prints a message on every add or remove operation."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend list and print notification with count of items added."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print notification then remove item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print notification of item being popped then remove it."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
