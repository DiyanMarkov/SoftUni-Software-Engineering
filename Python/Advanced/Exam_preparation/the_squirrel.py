rows = int(input())
commands = [x for x in input().split(", ")]

matrix = []

squirrel_pos = []

hazelnuts = 0

total_hazelnuts = 3

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    }

for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

    if "s" in current_row:
        squirrel_pos = [i, current_row.index("s")]
        matrix[squirrel_pos[0]][squirrel_pos[1]] = '*'


for command in commands:
    r = squirrel_pos[0] + directions[command][0]
    c = squirrel_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < rows):
        print(f"The squirrel is out of the field.")
        break


    if matrix[r][c] == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        break

    squirrel_pos = [r, c]

    if matrix[r][c] == "*":
        continue

    elif matrix[r][c] == "h":
        hazelnuts += 1

        matrix[r][c] = "*"

        if total_hazelnuts == hazelnuts:
            print(f"Good job! You have collected all hazelnuts!")
            break


else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")


#['left', 'left', 'up', 'right', 'up', 'up']

#['*', '*', 'h', '*', '*'],
#['t', '*', '*', '*', '*'],
#['*', 'h', '*', '*', '*'],
#['*', 'h', '*', 's', '*'],
#['*', '*', '*', '*', '*'],