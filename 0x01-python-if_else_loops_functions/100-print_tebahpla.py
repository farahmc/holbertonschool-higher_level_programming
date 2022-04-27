#!/usr/bin/python3

for a in reversed(range(97, 123)):
    if a % 2 != 0:
        a = a - 32
    print(chr(a), end="")
