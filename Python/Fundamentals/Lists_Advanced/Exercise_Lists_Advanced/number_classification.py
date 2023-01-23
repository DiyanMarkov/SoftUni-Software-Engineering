list_of_strings = input().split(', ')
positive_list = [str for str in list_of_strings if int(str) >= 0]
negative_list = [str for str in list_of_strings if int(str) < 0]
even_list = [str for str in list_of_strings if int(str) % 2 == 0]
odd_list = [str for str in list_of_strings if int(str) % 2 != 0]

print(f'Positive: {", ".join(positive_list)}')
print(f'Negative: {", ".join(negative_list)}')
print(f'Even: {", ".join(even_list)}')
print(f'Odd: {", ".join(odd_list)}')