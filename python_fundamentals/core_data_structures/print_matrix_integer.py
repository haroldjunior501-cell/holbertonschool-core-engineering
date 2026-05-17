#!/usr/bin/env python3
"""Function to print a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each row of the matrix on its own line, space-separated."""
    for row in matrix:
        print(" ".join("{:d}".format(x) for x in row))
