#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)  # Create a set to store unique integers
    sum_result = sum(unique_integers)  # Calculate the sum of unique integers
    return sum_result
