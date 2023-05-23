#!/usr/bin/python3
"""4. Text indentation - 5-text_indentation.py"""


def test_indentation(text):
    """
    This function prints a text w/ 2 new lines\
        after each: '.' '?' or ':'

    Args:
        text: text to use

    Raises:
        TypeError if text not a string

    Return:
        No return only print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new_text += text[i]
            new_text += "\n\n"
        else:
            new_text += text[i]
    print(new_text, end="")
