#!/usr/bin/python3
def uppercase(str):
    diff = abs(ord('A') - ord('a'))
    for ch in str:
        if ord(ch) <= ord('z') and ord(ch) >= ord('a'):
            ch = chr(ord(ch) - diff)
        print("{}".format(ch), end='')
    print()
