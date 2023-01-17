def final_number(operation_as_string, first_number, second_number):
    '''This is a function that applies specific operations between two numbers'''
    result = None
    if type_of_operation == 'multiply':
        result = first_number * second_number
    elif type_of_operation == 'divide':
        result = int(first_number / second_number)
    elif type_of_operation == 'add':
        result = first_number + second_number
    elif type_of_operation == 'subtract':
        result = first_number - second_number

    return result


type_of_operation = input()
first_number = int(input())
second_number = int(input())

print(final_number(type_of_operation, first_number, second_number))