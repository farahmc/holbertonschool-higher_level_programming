#!/bin/bash
# script that takes in a URL, sends a GET request to the URL with header variable and value
curl -s $1 -H "X-HolbertonSchool-User-Id: 98"
