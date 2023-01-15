list = input().split()
numbers_to_remove = int(input())

integer_list = []

for element in list:
   current_element = int(element)
   integer_list.append(current_element)

for element in range(numbers_to_remove):
    min_number = min(integer_list)
    integer_list.remove(min_number)


print(", ".join(str(x) for x in integer_list))
