#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import *
print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
