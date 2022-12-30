text = input()


sum = 0

for letter in text:
    if letter == 'a':
        sum = sum + 1
    elif letter == 'e':
        sum = sum + 2
    elif letter == 'i':
        sum = sum + 3
    elif letter == 'o':
        sum = sum + 4
    elif letter == 'u':
        sum = sum + 5

print(sum)

