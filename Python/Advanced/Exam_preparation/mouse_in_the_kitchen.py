rows, cols = [int(x) for x in input().split(',')]

matrix = []

mouse_pos = []

cheese_counter = 0

danger_activated = True

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    }

for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

    if 'M' in current_row:
        mouse_pos = [i, current_row.index('M')]
        matrix[mouse_pos[0]][mouse_pos[1]] = '*'

    elif 'C' in current_row:
        cheese_counter += current_row.count('C')


while True:
    direction = input()

    if direction == "danger":
        break

    r = mouse_pos[0] + directions[direction][0]
    c = mouse_pos[1] + directions[direction][1]

    if not (0 <= r < rows and 0 <= c < cols):
        matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
        danger_activated = False
        print("No more cheese for tonight!")
        break


    if matrix[r][c] == '@':
        continue

    mouse_pos = [r,c]

    if matrix[r][c] == 'C':
        matrix[r][c] = '*'
        cheese_counter -= 1

        if cheese_counter == 0:
            matrix[r][c] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            danger_activated = False
            break

    elif matrix[r][c] == '*':
        continue

    elif matrix[r][c] == 'T':
        matrix[r][c] = 'M'
        print("Mouse is trapped!")
        danger_activated = False
        break


if 'M' not in matrix:
    matrix[mouse_pos[0]][mouse_pos[1]] = 'M'

if danger_activated:
    print(f"Mouse will come back later!")

print('\n'.join([''.join(x) for x in matrix]))