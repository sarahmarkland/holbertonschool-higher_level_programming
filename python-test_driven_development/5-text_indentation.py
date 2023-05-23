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
    new_text = ""
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new_text += text[i]
            new_text += "\n\n"
        else:
            new_text += text[i]
    print(new_text, end="")
