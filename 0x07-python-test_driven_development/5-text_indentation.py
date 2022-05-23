#!/usr/bin/python3
def text_indentation(text):
    """
    Print 2 new lines after every instance of
    . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        raise ValueError("string cannot be empty")
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    if text[-1] == ".":
        text = text.replace(".", ".\n\n")
    if text[-1] == "?":
        text = text.replace("?", "?\n\n")
    if text[-1] == ":":
        text = text.replace(":", ":\n\n")
    print(text, end="")
