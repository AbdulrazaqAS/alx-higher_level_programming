#!/usr/bin/env python3
def uppercase(str):
    diff = abs(ord('A') - ord('a'))
    for ch in range(len(str)):
        if ord(str[ch]) <= ord('z') and ord(str[ch]) >= ord('a'):
            if ch == len(str) - 1:
                print("{:c}".format(ord(str[ch]) - diff), end='\n')
                break
            print('{:c}'.format(ord(str[ch]) - diff), end='')
        else:
            if ch == len(str) - 1:
                print('{}'.format(str[ch]), end='\n')
                break
            print('{}'.format(str[ch]), end='')
