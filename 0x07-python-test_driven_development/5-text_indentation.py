#!/usr/bin/python3
def text_indentation(text):
    """
    prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
                text (str): The text string to be parsed.

    Raises:
                TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    result = ''
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in separators and i < len(text) - 1 and text[i + 1] == ' ':
            result += '\n\n'
            i += 2
        else:
            i += 1

    print(result.strip())
