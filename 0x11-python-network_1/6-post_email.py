#!/usr/bin/python3
""" using requests package - takes in a URL and an email, sends a POST request
 to the passed URL with the email as a parameter, and displays the body of the
 response (decoded in utf-8) """
from requests import post
from sys import argv


data = {'email': argv[2]}
r = post(argv[1], data)
print(r.text)
