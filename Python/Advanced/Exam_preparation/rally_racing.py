rows = int(input())
racing_number = input()

matrix = []

car_pos = [0, 0]
tunnel_pos = []

km = 0

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)

    if "T" in current_row:
        tunnel_pos.append([row, current_row.index("T")])


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    }

command = input()

while command != "End":

    r = car_pos[0] + directions[command][0]
    c = car_pos[1] + directions[command][1]

    car_pos = [r, c]
    km += 10

    if matrix[r][c] == "T":
        matrix[r][c] = "."
        car_pos = [tunnel_pos[1][0], tunnel_pos[1][1]]
        matrix[car_pos[0]][car_pos[1]] = "."
        km += 20


    if matrix[r][c] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

matrix[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {km} km.")
[print(*row, sep="") for row in matrix]