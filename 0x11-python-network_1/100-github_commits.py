#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository “rails”
 by the user “rails” """
from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/"+argv[1]+"/"+argv[2]+"/commits"
    r = get(url)
    json_r = r.json()
    for data in json_r[:10]:
        print("{}: {}".format(data['sha'],
                              data['commit']['author']['name']))
