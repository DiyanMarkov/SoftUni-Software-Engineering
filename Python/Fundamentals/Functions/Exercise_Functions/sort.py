list_of_strings = input().split(' ')

integer_list = list(map(int, list_of_strings))
sorted_list = sorted(integer_list)
print(sorted_list)