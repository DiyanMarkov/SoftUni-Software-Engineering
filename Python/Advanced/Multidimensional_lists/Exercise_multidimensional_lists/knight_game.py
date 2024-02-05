def check_valid_index(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True

rows = int(input())
cols = rows

matrix = [[el for el in list(input())]for x in range(rows)]


removed_knights = 0
knights_positions = []

directions = {
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
}

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'K':
            knights_positions.append((row, col))

while True:
    greatest_knight = 0
    greatest_pos = []

    for row, col in knights_positions:
        current_knight = 0
        current_knight_pos = matrix[row][col]

        for direction in directions:
            movement_row, movement_col = row + direction[0], col + direction[1]

            if not check_valid_index(movement_row, movement_col):
                continue

            if matrix[movement_row][movement_col] == 'K':
                current_knight += 1

        if current_knight > greatest_knight:
            greatest_knight = current_knight
            greatest_pos = (row, col)

    if greatest_pos:  # проверяваме дали имаме кон за махане
        r, c = greatest_pos  # взимаме позицията на коня
        matrix[r][c] = "0"  # заменяме коня с 0
        removed_knights += 1
        knights_positions.remove((r,c))# увеличаваме броя на махнатите коне
    else:  # в противен случай, прекратяваме цикъла
        break

print(removed_knights)


# knights_postions -- > [(0, 1), (0, 3), (1, 0), (1, 4), (2, 2), (3, 0), (3, 4), (4, 1), (4, 3)]

#[
# ['0', 'K', '0', 'K', '0'],
# ['K', '0', '0', '0', 'K'],
# ['0', '0', 'K', '0', '0'],
# ['K', '0', '0', '0', 'K'],
# ['0', 'K', '0', 'K', '0']
#      ]