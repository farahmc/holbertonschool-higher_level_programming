# Python - More Classes

## Tasks

### 0. Simple rectangle
- Write an empty class `Rectangle` that defines a rectangle:

### 1. Real definition of a rectangle
- Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`

### 2. Area and Perimeter
- Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:

### 3. String representation
- Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`

### 4. Eval is magic
- Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

### 5. Detect instance deletion
- Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 6. How many instances
- Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 7. Change representation
- Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 8. Compare rectangles
- Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
  - Static method def `bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area

### 9. A square is a rectangle
- Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
  - Private instance attribute: `width`:
  - Private instance attribute: `height`:
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle area
  - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - `print()` and `str()` should print the rectangle with the character `#`
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
  - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
  - Static method def `bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - Class method `def square(cls, size=0):` that returns a new Rectangle instance with width == height == size
