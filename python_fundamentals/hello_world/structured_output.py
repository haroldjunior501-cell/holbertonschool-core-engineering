#!/usr/bin/env python3
"""Prints structured output with language info and a Pi approximation."""
pi = 3.14159
pi_approx = round(pi, 2)
is_valid = pi > 3

print("Language: Python")
print("Version: 3")
print(f"Pi approx: {pi_approx}")
print(f"Computation valid: {is_valid}")
