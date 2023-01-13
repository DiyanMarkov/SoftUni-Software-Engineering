number = int(input())
courses = []

for current_course_name in range(number):
    current_course_name = input()
    courses.append(current_course_name)
    #courses += [current_course_name]

print(courses)