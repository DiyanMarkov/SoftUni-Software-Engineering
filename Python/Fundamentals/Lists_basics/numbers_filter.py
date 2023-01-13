number = int(input())
full_list = []
filtered_list = []

for current_number in range(number):
    current_number = int(input())
    full_list.append(current_number)

command = input()
for number in full_list:

    if command == 'even' and number % 2 == 0:
        filtered_list.append(number)

    elif command == 'odd' and number % 2 != 0:
        filtered_list.append(number)

    elif command == 'negative' and number < 0:
        filtered_list.append(number)

    elif command == 'positive' and number >= 0:
        filtered_list.append(number)

print(filtered_list)