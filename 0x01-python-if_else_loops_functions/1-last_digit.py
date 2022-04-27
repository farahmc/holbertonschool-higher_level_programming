#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr(number)
last_number_string = number_string[-1]
last_number = int(last_number_string)

if number > 0 and last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
elif number < 0 and last_number != 0:
    print(f"Last digit of {number} is -{last_number} and is less than 6 and not 0")
elif number > 0 and last_number < 6 and last_number != 0:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_number} and is 0")
