record_seconds = float(input())
distance = float(input())
swimming_time_per_meter = float(input())

all_time = distance * swimming_time_per_meter

delay = distance // 15

times_slowed = delay * 12.5

total_time = all_time + times_slowed

difference = abs(total_time - record_seconds)

#Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
#" Yes, he succeeded! The new world record is {времето на Иван} seconds."

if total_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time: .2f} seconds.')

elif record_seconds <= total_time:
    print(f'No, he failed! He was {difference: .2f} seconds slower.')