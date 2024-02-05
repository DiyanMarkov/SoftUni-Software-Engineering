rows, cols = [int(x) for x in input().split()]

matrix = []

boy_pos = []


for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

    if "B" in current_row:
        boy_pos = [i, current_row.index("B")]
        pos_copy = boy_pos.copy()


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    }


while True:
    command = input()

    if command == '':
        break

    r = pos_copy[0] + directions[command][0]
    c = pos_copy[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        print(f"The delivery is late. Order is canceled.")
        matrix[boy_pos[0]][boy_pos[1]] = " "
        break

    if matrix[r][c] == '*':
        continue


    pos_copy = [r, c]

    if matrix[r][c] == '-':
        matrix[r][c] = '.'

    elif matrix[r][c] == 'P':
        matrix[r][c] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[r][c] == 'A':
        matrix[r][c] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

[print(*sub_list, sep="") for sub_list in matrix]