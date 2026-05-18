#!/usr/bin/env python3
"""Module defining Fish, Bird, and FlyingFish with multiple inheritance."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish with behaviors of both Fish and Bird."""

    def swim(self):
        """Print flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print flying fish flying behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
