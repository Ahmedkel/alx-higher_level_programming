#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0
    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)
            sum += element
    return sum
