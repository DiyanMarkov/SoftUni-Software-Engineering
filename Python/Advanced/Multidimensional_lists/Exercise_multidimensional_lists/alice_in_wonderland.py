def check_valid_index(r,c):
    if 0 <= r < rows and 0 <= c < rows:
        return True

rows = int(input())

matrix = [[int(el) if el.isdigit() else el for el in input().split()] for x in range(rows)]

alice_pos = []

for row in range(rows):
    for col in range(rows):

        if matrix[row][col] == 'A':
            alice_pos = [row,col]
            matrix[row][col] = '*'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

total_tea_bags = 0

while total_tea_bags < 10:
    command = input()

    movement_row, movement_col = alice_pos[0] + directions[command][0], alice_pos[1] + directions[command][1]

    if not check_valid_index(movement_row,movement_col):
        print("Alice didn't make it to the tea party.")
        [print(*sub_list, sep=" ") for sub_list in matrix]
        break

    if matrix[movement_row][movement_col] == 'R':
        if matrix[movement_row][movement_col] == 'R':
            matrix[movement_row][movement_col] = '*'
            print("Alice didn't make it to the tea party.")
            [print(*sub_list, sep=" ") for sub_list in matrix]
            break

    if matrix[movement_row][movement_col] != '.' and matrix[movement_row][movement_col] != '*':
        total_tea_bags += matrix[movement_row][movement_col]

    alice_pos = [movement_row,movement_col]
    matrix[movement_row][movement_col] = '*'

    if total_tea_bags >= 10:
        print(f"She did it! She went to the party.")
        [print(*sub_list, sep=" ") for sub_list in matrix]
        break