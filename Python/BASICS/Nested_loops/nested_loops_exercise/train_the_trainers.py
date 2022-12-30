num_jury = int(input())
presentation_name = input()

total_sum = 0
counter_presentations = 0

while presentation_name != 'Finish':

    sum_grades = 0
    for grade in range(num_jury):
        grade = float(input())
        sum_grades += grade
        total_sum += grade
        counter_presentations += 1

    average_grades = sum_grades / num_jury

    print(f"{presentation_name} - {average_grades:.2f}.")

    presentation_name = input()

average_from_all = total_sum / counter_presentations

print(f"Student's final assessment is {average_from_all:.2f}.")