n = int(input())


left_sum = 0

for i in range(0, n):
    current_sum = int(input())
    left_sum += current_sum

right_sum = 0

for i in range(0, n):
    current_sum = int(input())
    right_sum += current_sum

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')

else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')