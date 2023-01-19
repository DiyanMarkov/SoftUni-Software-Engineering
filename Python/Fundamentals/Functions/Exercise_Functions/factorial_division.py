def factorial(first, second):
    for num in range(1, first):
        first *= num

    for num in range(1, second):
        second *= num

    result = first / second
    return f'{result:.2f}'
first_number = int(input())
second_number = int(input())

print(factorial(first_number, second_number))