#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if divisor == 0:
                raise ZeroDivisionError
            division_result = dividend / divisor
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (ValueError, TypeError):
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result_list.append(division_result)
    return result_list
