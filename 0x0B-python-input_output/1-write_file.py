#!/usr/bin/python3
"""
Defines a function for text file-reading,
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write the provided text to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
