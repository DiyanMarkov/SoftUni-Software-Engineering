list_of_strings = input().split(' ')
even_strings = [str for str in list_of_strings if len(str) % 2 == 0]
print('\n'.join(even_strings))