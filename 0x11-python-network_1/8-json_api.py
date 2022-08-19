#!/usr/bin/python3
""" using requests package - takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter """
from requests import post
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    response = post('http://0.0.0.0:5000/search_user', data)
    try:
        j_response = response.json()
        if len(j_response.keys()) > 0:
            print("[{}] {}".format(j_response['id'], j_response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
