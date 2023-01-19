'''You will receive three integer numbers.
 Write a program that finds if their multiplication (the result) is negative,
 positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.'''

def multiplication_sign(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return 'zero'
    elif first < 0 and second < 0 and third < 0:
        return 'negative'
    elif first < 0 or second < 0 or third < 0:
        if first < 0 and second < 0 or first < 0 and third < 0 or  second < 0 and third < 0:
           return 'positive'
        return 'negative'
    elif first > 0 and second > 0 and third > 0:
        return 'positive'

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_sign(first_number, second_number, third_number))