#!/usr/bin/python3
""" using requests package - takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter """
from requests import post
from sys import argv


if len(sys.argv) > 1:
    data = {'q': argv[2]}
else:
    data = {'q': ""}
  
r = post('http://0.0.0.0:5000/search_user', data)
try:
    if len(r.json().keys()) > 0:
        print("[{}] {}".format(r.json('id'), r.json('name')))
    else:
        print("No result")
except:
    print("Not a valid JSON")
