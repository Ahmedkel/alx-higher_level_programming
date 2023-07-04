i#!/usr/bin/python3
"""
This module defines a function that prints a square made of '#' characters.
"""


def print_square(size):
    """
    Prints a square made of '#' characters.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
