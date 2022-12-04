#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of', number, 'is', end=" ")
sign = -1 if number < 0 else 1
number = abs(number) % 10
number *= sign
if number > 5:
    print(number, 'and is greater than 5')
elif number == 0:
    print(number, 'and is 0')
else:
    print(number, 'and is less than 6 and not 0')
