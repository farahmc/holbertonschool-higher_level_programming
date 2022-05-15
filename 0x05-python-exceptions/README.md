# Python - Exceptions

## Tasks

### 0. Safe list printing
Write a function that prints x elements of a list.
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- You have to use `try:` / `except:`

### 1. Safe printing of an integers list
Write a function that prints an integer with "{:d}".format().
- Prototype: `def safe_print_integer(value):`
- You have to use `try:` / `except:`
- You are not allowed to use `type()`

### 2. Print and count integers
Write a function that prints the first x elements of a list and only integers.
- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- You have to use `try:` / `except:`
- You are not allowed to use `len()`

### 3. Integers division with debug
Write a function that divides 2 integers and prints the result.
- Prototype: `def safe_print_division(a, b):`
- The result of the division should print on the `finally:` section preceded by `Inside result:`

### 4. Divide a list
Write a function that divides element by element 2 lists.
- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- You have to use `try:` / `except:` / `finally:`

### 5. Raise exception
Write a function that raises a type exception.
- Prototype: `def raise_exception():`

### 6. Raise a message
Write a function that raises a name exception with a message.
- Prototype: `def raise_exception_msg(message=""):`