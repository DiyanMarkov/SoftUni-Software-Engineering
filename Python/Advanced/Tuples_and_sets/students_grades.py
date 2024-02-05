from statistics import mean

times = int(input())

all_students = {}

for i in range(times):
    name, grade = input().split()
    grade = float(grade)
    if name not in all_students:
        all_students[name] = []

    all_students[name].append(grade)


for key,value in all_students.items():
    average = sum(value) / len(value)
    print(f"{key} -> {' '.join([str(f'{x:.2f}') for x in value])} (avg: {average:.2f})")