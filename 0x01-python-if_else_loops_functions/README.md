# Python - If, Else, Loops, Functions

## Tasks

### 0. Positive anything is better than negative nothing
This program will assign a random signed number to the variable number each time
it is executed. Complete the source code in order to print whether the number
stored in the variable number is positive or negative.

### 1. The last digit
This program will assign a random signed number to the variable number each time
it is executed. Complete the source code in order to print the last digit of the
number stored in the variable number.

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
Write a program that prints the ASCII alphabet, in lowercase, not followed by a
new line.

### 3. When I was having that alphabet soup, I never thought that it would pay off
Write a program that prints the ASCII alphabet, in lowercase, not followed by a
new line.

### 4. Hexadecimal printing
Write a program that prints all numbers from 0 to 98 in decimal and in
hexadecimal

### 5. 00...99
Write a program that prints numbers from 0 to 99.

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
Write a program that prints all possible different combinations of two digits.

### 7. islower
Write a function that checks for lowercase character.

### 8. To uppercase
Write a function that prints a string in uppercase followed by a new line.

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with
them that's important
Write a function that prints the last digit of a number.
- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit

### 10. a + b
Write a function that adds two integers and returns the result.
- Prototype: `def add(a, b):`
- Returns the value of a + b

### 11. a ^ b
Write a function that computes a to the power of b and return the value.
- Prototype: `def pow(a, b):`
- Returns the value of a ^ b

### 12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.
- For multiples of three print `Fizz` instead of the number and for multiples of
five print `Buzz`.
- For numbers which are multiples of both three and five print `FizzBuzz`.
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space
- You are not allowed to import any module

### 13. Insert in sorted linked list
Write a function in C that inserts a number into a sorted singly linked list.

### 14. Smile in the mirror
Write a program that prints the ASCII alphabet, in reverse order, alternating
lowercase and uppercase (z in lowercase and Y in uppercase), not followed by a
new line.
- You can only use one `print` function
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

### 15. Remove at position
Write a function that creates a copy of the string, removing the character at
the position `n`
- Prototype: `def remove_char_at(str, n):`
- You are not allowed to import any module

### 16. ByteCode -> Python #2
Write the Python function `def magic_calculation(a, b, c):` that does exactly
the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```