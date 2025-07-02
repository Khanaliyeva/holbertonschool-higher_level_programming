#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
then saves them to a JSON file using provided functions."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all arguments from command line (excluding the script name)
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
