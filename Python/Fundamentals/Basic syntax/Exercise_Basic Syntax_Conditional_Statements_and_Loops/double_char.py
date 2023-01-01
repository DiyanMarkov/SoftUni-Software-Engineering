command = ''
upgraded_string = ''

while command != 'End':
    original_string = input()
    if original_string == 'SoftUni':
        continue
    for i in original_string:
        upgraded_string = upgraded_string + i*2

    print(upgraded_string)




