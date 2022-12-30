number_of_groups = int(input())

sum_people_1 = 0
sum_people_2 = 0
sum_people_3 = 0
sum_people_4 = 0
sum_people_5 = 0

total_people = 0

for people in range(number_of_groups):
    current_people = int(input())
    if current_people <= 5:
        sum_people_1 += current_people

    elif current_people <= 12:
        sum_people_2 += current_people

    elif current_people <= 25:
        sum_people_3 += current_people

    elif current_people <= 40:
        sum_people_4 += current_people

    elif current_people >= 41:
        sum_people_5 += current_people


total_people = sum_people_1 + sum_people_2 + sum_people_3 + sum_people_4 + sum_people_5

percent1 = sum_people_1 / total_people * 100
percent2 = sum_people_2 / total_people * 100
percent3 = sum_people_3 / total_people * 100
percent4 = sum_people_4 / total_people * 100
percent5 = sum_people_5 / total_people * 100

print(f'{percent1:.2f}%')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{percent5:.2f}%')



