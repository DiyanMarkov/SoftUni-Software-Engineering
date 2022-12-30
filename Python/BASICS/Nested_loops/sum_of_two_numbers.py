i = int(input())
j = int(input())
magical_number = int(input())

is_found = False
count = 0

for number in range(i, j + 1):
    for second_number in range(i, j + 1):
        sum = number + second_number
        count += 1

        if sum == magical_number:
            is_found = True
            print(f'Combination N:{count} ({number} + {second_number} = {magical_number})')
            break

    if is_found == True:
        break

if is_found == False:
    print(f'"{count} combinations - neither equals {magical_number}"')


