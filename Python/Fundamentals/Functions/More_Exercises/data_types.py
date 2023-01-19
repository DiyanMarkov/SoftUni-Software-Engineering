"""Write a function that, depending on the first line of the input, reads one of the following strings:
 "int", "real", or "string".

· If the data type is an int, multiply the number by 2.
· If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
· If the data type is a string, surround the input with "$"."""

def what_data_type(string, number):
    if string == 'int':
        number = int(number)
        number *= 2
    if string == 'real':
        number = float(number)
        number *= 1.5
        number = f'{number:.2f}'
    if string == 'string':
        number = f'${number}$'
    return number


first_string = input()
second_string = input()
print(what_data_type(first_string, second_string))