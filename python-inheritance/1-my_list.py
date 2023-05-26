#!/usr/bin/python3
#baby class
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
