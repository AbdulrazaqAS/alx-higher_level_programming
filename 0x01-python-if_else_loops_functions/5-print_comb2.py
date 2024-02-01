#!/usr/bin/python3
for var in range(0, 100):
    if var == 99:
        print('99')
    else:
        print('{:02d}'.format(var), end=', ')
