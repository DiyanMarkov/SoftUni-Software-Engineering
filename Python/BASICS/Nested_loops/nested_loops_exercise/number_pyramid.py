number = int(input())

counter = 1
is_bigger_than_number = False

for rows in range (1, number + 1):
    for columns in range (1, rows + 1):
        print(counter, end=' ')
        counter += 1
        if counter > number:
            is_bigger_than_number = True
            break

    if is_bigger_than_number:
        break

    print()


