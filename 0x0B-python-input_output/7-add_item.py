#!/usr/bin/python3
"""
Script to add all arguments to a Python list
and saved as a JSON representation in a file
"""


import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
newfile = "add_item.json"

if os.path.exists(newfile) is False:
    save_to_json_file([], newfile)

arg_list = load_from_json_file(newfile)
for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])
save_to_json_file(arg_list, newfile)
