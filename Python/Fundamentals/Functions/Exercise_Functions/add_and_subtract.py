def sum_numbers(first, second):
    return first + second

def subtract(sum, third):
    return sum - third

def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result_subtract = subtract(sum_of_first_and_second_integers, third)
    return result_subtract


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))