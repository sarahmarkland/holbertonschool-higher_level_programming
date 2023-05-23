#!/usr/bin/python3
"""4. Text indentation - 5-text_indentation.py"""


def test_indentation(text):
    """test_indentation: function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text (str): text to print
    Returns:
        nothing
    Raises:
        TypeError: if text is not a string
    Doctest Examples:
        see dir: /tests/5-text_indentation.txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = True

    for char in text:
        if char != ' ' or new_line is False:
            print(char, end='')
            new_line = False
        elif char != ' ':
            new_line = False

        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
