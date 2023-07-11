#!/usr/bin/python3
"""Defines a function for file-appending."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file
       and returns the character count.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.

    Returns:
        int: Number of characters appended.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
