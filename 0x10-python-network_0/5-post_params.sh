#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL with 2 parameters and values
curl -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
