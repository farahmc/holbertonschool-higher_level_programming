#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv) - 1
    if args == 3:
        first = int(sys.argv[1])
        op = sys.argv[2]
        second = int(sys.argv[3])
        if op == '+':
            print(f"{first} + {second} = {add(first, second)}")
        elif op == '-':
            print(f"{first} - {second} = {sub(first, second)}")
        elif op == '*':
            print(f"{first} * {second} = {mul(first, second)}")
        elif op == '/':
            print(f"{first} / {second} = {div(first, second)}")
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
