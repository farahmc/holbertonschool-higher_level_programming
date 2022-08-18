#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
 the email as a parameter, and displays the body of the response (decoded in
 utf-8) """
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/post_email'
    values = {'email': 'me@gmail.com'}
    url_data = urlencode(values)
    data = url_data.encode('utf-8')
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read())
