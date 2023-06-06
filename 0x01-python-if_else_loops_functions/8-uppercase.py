#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        asc_ch = ord(ch)

        uppercase_ch = chr(asc_ch - 32) if 97 <= asc_ch <= 122 else ch
        print(uppercase_ch, end="")
    print()
