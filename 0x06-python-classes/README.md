# Python - Classes and Objects

## Tasks

### 0. My first square
Write an empty class `Square` that defines a square

## 1. Square with size
Write a class `Square` that defines a square (based on `0-square.py`) by:
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)

## 2. Size validation
Write a class `Square` that defines a square (based on `1-square.py`) by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`

### 3. Area of a square
Write a class `Square` that defines a square (based on `2-square.py`) by:
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area

### 4. Access and update private attribute
Write a class `Square` that defines a square (based on `3-square.py`) by:
- Private instance attribute: `size:`
  	  - property `def size(self):` to retrieve it
	  - property setter `def size(self, value):` to set it
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area

### 5. Printing a square
Write a class `Square` that defines a square (based on `4-square.py`) by:
- Private instance attribute: `size:`
  	  - property def `size(self):` to retrieve it
	  - property setter `def size(self, value):` to set it

### 6. Coordinates of a square
Write a class `Square` that defines a square (based on `5-square.py`) by:
- Private instance attribute: `size:`
- Private instance attribute: `position:`
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
