#!/usr/bin/python3
"""
Function to insert a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text to a file, after each line
    containing a specific string

    Arguments:
    filename - the file to open and append to
    search_string - the string to find, append a new string in the next line
    new_string - the string to append
    """
    new_str = ""
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            new_str += line
            if search_string in line:
                new_str += new_string
    with open(filename, 'w', encoding="utf-8") as newfile:
        newfile.write(new_str)

        #        if search_string in f:
        #            write_file = f.write(new_string)
