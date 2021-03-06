#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    l = len(argv)

    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    oper = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if oper == '+':
        print("{:d} + {:d} = {}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
    elif oper == '/':
        print("{:d} / {:d} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
