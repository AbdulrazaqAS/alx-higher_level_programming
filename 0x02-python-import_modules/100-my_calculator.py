#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    if c == '+':
        res = calc.add(a, b)
    elif c == '-':
        res = calc.sub(a, b)
    elif c == '*':
        res = calc.mul(a, b)
    elif c == '/':
        res = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {c} {b} = {res}")
