number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' ')
    event = command[0]
    people = command[-1]

    if event == 'add':
        train[-1] += int(people)
    elif event == 'insert':
        index = int(command[1])
        train[index] += int(people)

    elif event == 'leave':
        index = int(command[1])
        train[index] -= int(people)

print(train)