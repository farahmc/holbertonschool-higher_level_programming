#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the
 response (decoded in utf-8) """
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print(error.status)
