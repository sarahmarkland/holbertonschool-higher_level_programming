#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple (or use 0 if the tuple is smaller)
    a1, a2 = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b1, b2 = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]

    # Perform the addition of the corresponding elements
    sum_1 = a1 + b1
    sum_2 = a2 + b2

    # Return the result as a tuple
    return sum_1, sum_2
