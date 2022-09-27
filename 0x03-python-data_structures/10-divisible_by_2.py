#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        if (i % 2 == 1):
            return False
        if (i % 2 == 0):
            return True
        else:
            new_list = i
            return new_list
