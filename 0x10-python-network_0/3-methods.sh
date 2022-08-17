#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -i -X OPTIONS "$1" | grep 'Allow' | awk -F': ' '{print $2}'
