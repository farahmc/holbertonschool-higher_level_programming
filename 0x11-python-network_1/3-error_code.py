#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the
 response (decoded in utf-8) """
import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print(f"Error code: {}".format(error.status))
