def all_characters_in_between(first, second):
    for char in range(ord(first) + 1, ord(second)):
        list_characters.append(chr(char))
    return list_characters

first_character = input()
second_character = input()

list_characters = []
result = all_characters_in_between(first_character, second_character)
print(' '.join(result))
