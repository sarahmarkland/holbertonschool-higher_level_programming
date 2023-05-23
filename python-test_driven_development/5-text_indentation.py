#!/usr/bin/python3
"""3. Text indentation - Write func that prints text with 2 new line after: .,?:"""


def test_indentation(text):
    """test_indentation: func that prints text with 2 new line after: .,?:"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end="")
