#!/usr/bin/python3

for i in range(26, 0, -1):
    alpha = i + (ord('A') - 1)
    if i % 2 == 0:
        alpha += 32
    print('{}'.format(chr(alpha)), end='')
