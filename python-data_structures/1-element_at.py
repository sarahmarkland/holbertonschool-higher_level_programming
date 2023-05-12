#!/usr/bin/python3
def element_at(my_list, idx):
    for item in my_list:
        if idx < 0 OR idx > len(my_list):
            return None
        else:
            return item
