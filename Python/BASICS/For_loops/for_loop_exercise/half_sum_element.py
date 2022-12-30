import sys

n = int(input())

max_sum = -sys.maxsize
sum_all = 0

for number in range (n):
    current_number = int(input())
    sum_all += current_number

    if current_number > max_sum:
     max_sum = current_number

if max_sum == sum_all - max_sum:
    print(f'Yes')
    print(f'Sum = {max_sum}')

else:
    print('No')
    difference = abs(max_sum - (sum_all-max_sum))
    print(f'Diff = {difference}')
