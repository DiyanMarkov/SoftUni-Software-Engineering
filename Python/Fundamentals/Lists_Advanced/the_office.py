employees_happiness = input().split(' ')
factor = int(input())



multiplication_of_happiness = list(map(lambda x: int(x) * factor, employees_happiness))
sum = 0

for i in multiplication_of_happiness:
    sum += i

average = sum / len(multiplication_of_happiness)

happy_count = [num for num in multiplication_of_happiness if num > average]
total_count = len(multiplication_of_happiness)

counter_happiness = len(happy_count)

if counter_happiness >= total_count/2:
    print(f"Score: {counter_happiness}/{total_count}. Employees are happy!")
else:
    print(f"Score: {counter_happiness}/{total_count}. Employees are not happy!")