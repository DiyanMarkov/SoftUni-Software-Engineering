number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0

odd_or_even = 'odd'

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2

    if result % 2 == 0:
        odd_or_even = 'even'
    print(f'{number_1} {operator} {number_2} = {result} - {odd_or_even}')

elif operator == '/' or operator == '%':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        if operator == '/':
            result = number_1 / number_2
            print(f'{number_1} / {number_2} = {result:.2f}')
        elif operator == '%':
            result = number_1 % number_2
            print(f'{number_1} % {number_2} = {result}')

