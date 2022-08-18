#!/usr/bin/python3
""" script that fetches URL using package requests"""
from requests import get
from sys import argv
from urllib.error import HTTPError


try:
    r = get(argv[1])
    print("r.text")
except HTTPError as error:
    print("Error code: {}".format(r.status_code))
