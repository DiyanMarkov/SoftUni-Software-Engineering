starting_character = int(input())
ending_character = int(input())
current_character = 0

for character in range(starting_character, ending_character + 1):
    current_character += character
    print(chr(current_character), end=' ')
    current_character = 0