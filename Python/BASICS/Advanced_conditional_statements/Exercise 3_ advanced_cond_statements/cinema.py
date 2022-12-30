screening_type = input()
rows = int(input())
columns = int(input())

premiere = 12
normal = 7.50
discount = 5

price = 0
if screening_type == 'Premiere':
    price = rows * columns * premiere

if screening_type == 'Normal':
    price = rows * columns * normal

if screening_type == 'Discount':
    price = rows * columns * discount

all_income = price


print(f'{all_income:.2f} leva')