def abs_numbers(number):
    result = [abs(num) for num in number]
    return result

list_of_numbers = list(map(float, input().split(' ')))
print(abs_numbers(list_of_numbers))

#######################################
#numbers = list(map(float, input().split(' ')))
#result = [abs(num) for num in numbers]
#print(result)

#######################################
#numbers = input().split(' ')
#abs_list = []

#for num in numbers:
    #abs_list.append(abs(float(num)))

#print(abs_list)


