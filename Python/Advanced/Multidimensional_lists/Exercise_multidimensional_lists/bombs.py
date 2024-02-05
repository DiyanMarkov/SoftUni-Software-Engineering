n = int(input())

matrix = [[int(el) for el in input().split()] for x in range(n)]
coordinates = [[int(coordinate) for coordinate in tuple.split(",")] for tuple in input().split()]

directions = (
    (-1, 0),  # up
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (1, -1),  # down-left
    (1, 1),  # down-right
    (0, 0),  # current-position // explode the bomb itself after all other directions!!!
)


for row, col in coordinates:  # row, col --> direction of bomb

    if matrix[row][col] < 0: # check if bomb will explode
        continue

    for x, y in directions:
        r, c = row + x, col + y   # r, c --> current direction

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0  # detonate bomb on current direction


alive_cells = [num for row in matrix for num in row if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*matrix[r], sep=" ") for r in range(n)]

#[
# [8, 3, 2, 5],
# [6, 4, 7, 9],
# [9, 9, 3, 6],
# [6, 8, 1, 2]
#    ]

# [[1, 2], [2, 1], [2, 0]]