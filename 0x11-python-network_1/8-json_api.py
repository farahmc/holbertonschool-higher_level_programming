#!/usr/bin/python3
""" using requests package - takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter """
from requests import post
from sys import argv


if len(sys.argv) > 1 and type(sys.argv[2]) is str:
    data = {'q': argv[2]}
    r = post('http://0.0.0.0:5000/search_user', data)
    print("[{}] {}".format(r.json('id'), r.json('name')))
else:
    data = {'q': ""}
    print("No result")
