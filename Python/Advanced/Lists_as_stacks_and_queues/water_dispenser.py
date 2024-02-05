from collections import deque

quantity = int(input())

people = deque()

while True:
    command = input()
    if command == 'Start':
        break

    people.append(command)

while True:
    command = input()
    if command == 'End':
        break

    if len(command) > 1:
        command = command.split()
        quantity += int(command[1])
    else:
        person = people.popleft()
        if int(command) > quantity:
            print(f"{person} must wait" )
        else:
            print(f"{person} got water")
            quantity -= int(command[0])

print(f'{quantity} liters left')