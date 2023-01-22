list_of_strings = input().split(', ')

sorted_list = sorted(list_of_strings, key=lambda x: (-len(x), x))
print(sorted_list)