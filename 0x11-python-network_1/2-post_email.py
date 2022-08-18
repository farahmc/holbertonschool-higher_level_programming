#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
 the email as a parameter, and displays the body of the response (decoded in
 utf-8) """
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    url_data = urlencode(values)
    data = url_data.encode('utf-8')
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
