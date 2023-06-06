#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    return num - (10 * int(num/10))


helper = last_digit(number)
if helper > 5 and helper != 0:
    print('Last digit of', number, 'is', helper, 'and is greater than 5')

if helper == 0:
    print('Last digit of', number, 'is', helper, 'and is 0')

if helper < 6 and helper != 0:
    print('Last digit of', number, 'is', helper, 'and is less '
          'than 6 and not 0')
