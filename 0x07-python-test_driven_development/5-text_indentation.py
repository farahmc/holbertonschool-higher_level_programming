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
    text = text.translate({ord('.'):'.\n', ord('?'):'?\n', ord(':'):':\n'})
    new = ''.join([line.strip()+'\n\n' for line in text.splitlines()])
    if new[-1] == "\n" and new[-1] != "?":
        new = new.rstrip('\n')
    print(new, end="")
