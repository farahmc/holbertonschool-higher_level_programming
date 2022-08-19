#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the GitHub
 API to display your id """
from requests import get
from sys import argv

if __name__ == "__main__":
    try:
        r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        json_r = r.json()
        print(json_r['id'])
    except:
        print("None")
