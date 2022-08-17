#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -i "$1" | grep 'Content-Length:' | awk '{print $2}'
