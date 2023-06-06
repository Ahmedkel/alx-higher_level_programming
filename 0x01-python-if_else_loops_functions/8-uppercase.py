#!/usr/bin/python3
def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
        s: a string

    Returns:
        None.
    """
    for c in s:
        if 97 <= ord(c) <= 122:
            uppercase_c = chr(ord(c) - 32)
        else:
            uppercase_c = c
        print("{:s}".format(uppercase_c), end="")
    print()
