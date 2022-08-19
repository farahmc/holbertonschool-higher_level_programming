#!/usr/bin/python3
""" using requests package - takes in a URL, sends a request to the URL and
 displays the value of the X-Request-Id variable found in the header of the
 response """
from requests import get
from sys import argv

if __name__ == "__main__":
    r = get(argv[1])
    print(r.headers['X-Request-Id'])
