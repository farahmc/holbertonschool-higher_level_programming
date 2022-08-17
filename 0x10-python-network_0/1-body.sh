#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the 200 response only
curl -s -L "$1"
