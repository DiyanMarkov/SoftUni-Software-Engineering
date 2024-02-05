n = int(input())

commands = input().split() # "left", "right", "up", "down"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    }

matrix = []
miner_pos = []
total_coal, collected_coal = 0, 0

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[row][miner_pos[1]] = '*'

    total_coal += matrix[row].count('c')

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1] # get the coordinates (r,c)

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == 'c':
        collected_coal += 1
        matrix[r][c] = '*'

    elif matrix[r][c] == '*':
        continue

    if matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        exit()


    if collected_coal == total_coal:
        print(f"You collected all coal! ({r}, {c})")
        exit()


print(f"{total_coal-collected_coal} pieces of coal left. ({r}, {c})")

# up right right up right
#[
# ['*', '*', '*', 'c', '*'],
# ['*', '*', '*', 'e', '*'],
# ['*', '*', 'c', '*', '*'],
# ['s', '*', '*', 'c', '*'],
# ['*', '*', 'c', '*', '*'],
#                            ]
