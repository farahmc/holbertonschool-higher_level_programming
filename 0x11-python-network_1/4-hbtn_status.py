#!/usr/bin/python3
""" script that fetches URL using package requests"""
from requests import get


r = get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
