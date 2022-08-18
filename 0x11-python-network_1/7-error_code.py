#!/usr/bin/python3
""" script that fetches URL using package requests"""
from requests import get
from sys import argv


r = get(argv[1])

if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)
