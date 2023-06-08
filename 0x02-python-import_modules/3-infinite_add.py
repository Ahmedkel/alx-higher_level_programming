#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of numbers of arguments passed"""
import sys

args = sys.argv[1:]
sum_of_args = sum(map(int, args))

print(sum_of_args)
