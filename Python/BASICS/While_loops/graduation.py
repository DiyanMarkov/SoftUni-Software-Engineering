student_name = input()

if_graduated = False
break_times = 0

end_grade = 0
year = 1

while year <= 12:
    if break_times > 1:
        is_graduated = False
        break

    current_grade = float(input())


    if current_grade >= 4:
        end_grade += current_grade
        year += 1
        is_graduated = True

    if current_grade < 4:
        break_times += 1
        #if break_times > 1:
            #is_graduated = False
            #break
    continue

average_grade = end_grade / 12

if is_graduated == True:
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')

else:
    print(f'{student_name} has been excluded at {year} grade')



