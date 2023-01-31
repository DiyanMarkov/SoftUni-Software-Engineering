number_of_people = int(input())
elevator_capacity = int(input())

elevator_courses = 0

while number_of_people > 0:
    number_of_people -= elevator_capacity
    elevator_courses += 1

print(elevator_courses)


#from math import ceil
#elevator_courses = 0
#if elevator_courses != 0:
 #elevator_courses = ceil(number_of_people / elevator_capacity)
#print(elevator_courses)