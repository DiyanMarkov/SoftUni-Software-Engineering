list_of_strings = input().split(' ')
palindrome = input()

palindrome_list = [string for string in list_of_strings if string[0] == string[-1]]
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')