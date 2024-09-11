#!/usr/bin/python3
"""
prints text with 2 lines after . ? :
"""
def text_indentation(text):
    """
    Args:
        text: string

    Raises:
        TypeError: if not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i =+ 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
