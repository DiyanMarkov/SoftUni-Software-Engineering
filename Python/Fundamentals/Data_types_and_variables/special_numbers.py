number = int(input())
sum_number = 0
for i in range(1, number + 1):
    i = str(i)
    for current_digit in i:
        current_digit = int(current_digit)
        sum_number += current_digit
    if sum_number == 5 or sum_number == 7 or sum_number == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
    sum_number = 0