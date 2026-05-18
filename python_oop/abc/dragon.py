#!/usr/bin/env python3
"""Module defining SwimMixin, FlyMixin, and Dragon using mixins."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
