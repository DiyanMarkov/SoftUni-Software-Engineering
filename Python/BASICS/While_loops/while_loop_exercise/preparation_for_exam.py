unwanted_grades_number = int(input())

average_score = 0
total_exercises = 0
name_of_exercise = ''
sum_grades = 0
bad_grade_counter = 0
last_problem = ''

if_enough = False

while bad_grade_counter < unwanted_grades_number:
    name_of_exercise = input()
    if name_of_exercise == 'Enough':
        if_enough = True
        break

    grade = int(input())

    if grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == unwanted_grades_number:
            break

    sum_grades += grade
    total_exercises += 1
    last_problem = name_of_exercise

average_score = sum_grades / total_exercises

if if_enough == True:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {total_exercises}')
    print(f'Last problem: {last_problem}')
else:
    print(f'You need a break, {unwanted_grades_number} poor grades.')
