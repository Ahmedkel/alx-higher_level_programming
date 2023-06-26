#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem1 = my_list_1[i]
        except IndexError:
            print("out of range")
            elem1 = 1
        try:
            elem2 = my_list_2[i]
        except IndexError:
            print("out of range")
            elem2 = 1
        try:
            division = elem1 / elem2
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        result.append(division)
    return result
