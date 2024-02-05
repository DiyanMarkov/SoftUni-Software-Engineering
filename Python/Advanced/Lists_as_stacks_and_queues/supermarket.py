from collections import deque

q = deque()

while True:
    command = input()
    if command == 'End':
        break

    if command == 'Paid':
        print('\n'.join(q))
        q.clear()
    else:
        q.append(command)

print(f'{len(q)} people remaining')