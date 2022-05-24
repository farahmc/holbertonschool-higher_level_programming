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

    text = text.translate({ord('.'): '.\n', ord('?'): '?\n', ord(':'): ':\n'})
    new = ''.join([line.strip()+'\n\n' for line in text.splitlines()])
    new = new.rstrip('\n')

    if new[-1] == "?" or new[-1] == "." or new[-1] == ":":
        new += "\n\n"
    print(new, end="")
