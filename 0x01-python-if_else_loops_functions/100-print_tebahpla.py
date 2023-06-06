#!/usr/bin/python3
upper_chk = True

for i, j in zip(range(122, 96, -1), range(90, 64, -1)):
    if upper_chk != True:
        print("{:c}".format(j).upper(), end="")
    else:
        print("{:c}".format(j).lower(), end="")
    upper_chk = not upper_chk
