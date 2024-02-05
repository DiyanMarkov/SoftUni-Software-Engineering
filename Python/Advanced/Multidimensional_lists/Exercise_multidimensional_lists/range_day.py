def check_valid_index(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True

def move(direction, steps):
    r, c = shooter_pos[0] + (directions[direction][0] * int(steps)), shooter_pos[1] + (directions[direction][1] * int(steps))

    if not check_valid_index(r, c):
        return shooter_pos

    if matrix[r][c] == 'x':
        return shooter_pos

    return [r, c]

def shoot(direction):
    r, c = shooter_pos[0] + directions[direction][0] , shooter_pos[1] + directions[direction][1]

    while check_valid_index(r, c):

        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r,c]

        r += directions[direction][0]
        c += directions[direction][1]


rows, cols = 5, 5

matrix = []

shooter_pos = []
targets_pos = []
targets_count = 0
targets_hit = []


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):

        if matrix[row][col] == 'A':
            shooter_pos = [row, col]


        elif matrix[row][col] == 'x':
            targets_count += 1
            targets_pos.append([row, col])


for _ in range(int(input())):
    command, *data = input().split()


    if command == 'move':
        shooter_pos = move(data[0], data[1])

    elif command == 'shoot':
        target_down_pos = shoot(data[0])

        if target_down_pos:
            targets_hit.append(target_down_pos)

        if len(targets_hit) == targets_count:
            print(f'Training completed! All {targets_count} targets hit.')
            break

if len(targets_hit) < targets_count:
    print(f'Training not completed! {targets_count - len(targets_hit)} targets left.')

print(*targets_hit, sep="\n")