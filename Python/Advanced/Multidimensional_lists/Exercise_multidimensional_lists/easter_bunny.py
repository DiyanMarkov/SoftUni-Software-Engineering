size = int(input())

matrix = []

traps_position = []
bunny_position = []
best_path = []
best_direction = None

total_eggs = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'B' in matrix[row]:
        bunny_position = [row, matrix[row].index('B')]


for direction, positions in directions.items():
    r = bunny_position[0] + positions[0]
    c = bunny_position[1] + positions[1]

    current_path = []
    current_eggs = 0

    while 0 <= r < size and 0 <= c < size:

        if matrix[r][c] == 'X':
            current_pos = bunny_position
            break

        current_eggs += int(matrix[r][c])
        current_path.append([r, c])

        r += positions[0]
        c += positions[1]

    if current_eggs >= total_eggs:
        total_eggs = current_eggs
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(total_eggs)