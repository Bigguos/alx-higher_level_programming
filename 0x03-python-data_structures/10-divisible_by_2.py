#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if (i % 2 == 1):
            new_list.append(True)
        if (i % 2 == 0):
            new_list.append(True)
    return new_list
