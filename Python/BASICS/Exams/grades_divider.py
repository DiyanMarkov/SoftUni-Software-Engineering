students = int(input())

counter_less_than_3 = 0
counter_less_than_3_99 = 0
counter_less_than_4_99 = 0
counter_greater_5 = 0

total_grades = 0

for i in range(students):
    grade = float(input())
    total_grades += grade

    if grade < 3:
        counter_less_than_3 += 1
    elif grade <= 3.99:
        counter_less_than_3_99 += 1
    elif grade <= 4.99:
        counter_less_than_4_99 += 1
    elif grade >= 5:
        counter_greater_5 += 1

average_grade = total_grades / students

percent_5 = (counter_greater_5 / students) * 100
percent_4_99 = (counter_less_than_4_99 / students) * 100
percent_3_99 = (counter_less_than_3_99 / students) * 100
percent_3 = (counter_less_than_3 / students) * 100


print(f"Top students: {percent_5:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4_99:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3_99:.2f}%")
print(f"Fail: {percent_3:.2f}%")
print(f"Average: {average_grade:.2f}")
