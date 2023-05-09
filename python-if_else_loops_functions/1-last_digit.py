#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10)
str1 = "Last digit of "
str2 = "is "
greater_str = "and is greater than 5"
zero_str = "and is 0"
less_str = "and is less than 6 and not 0"
if(number < 0):
    last_digit *= -1
if last_digit > 5:
    print(str1 + str(number) + " " + str2 + str(last_digit) + " " + greater_str)
elif last_digit == 0:
    print(str1 + str(number) + " " + str2 + str(last_digit) + " " + zero_str)
else:
    print(str1 + str(number) + " " + str2 + str(last_digit) + " " + less_str)
