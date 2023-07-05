#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these
    special characters : ., ? and :

    Args:
                text (str): The text string.

    Raises:
                TypeError: If is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for delimeter in ".?:":
        l_text = s.split(delimeter)
        s = ""
        for i in l_text:
            i = i.strip(" ")
            s = i + delimeter if s is "" else s + "\n\n" + i + delimeter

    print(s[:-3], end="")
