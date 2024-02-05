rows = 6
cols = 6

matrix = []

rover_pos = []

deposits = {"W": ["Water", 0], "C": ["Concrete", 0], "M": ["Metal", 0]}

directions = {
    'up': lambda r, c: [(r - 1) % 6, c],
    'down': lambda r, c: [(r + 1) % 6, c],
    'left': lambda r, c: [r, (c - 1) % 6],
    'right': lambda r, c: [r, (c + 1) % 6],
}

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)

    if "E" in current_row:
        rover_pos = (row, current_row.index('E'))

commands = input().split(", ")

for command in commands:
    rover_pos = directions[command](*rover_pos)
    position = matrix[rover_pos[0]][rover_pos[1]]

    if position in deposits:
        print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        deposits[position][1] += 1

    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
    print(f"Area suitable to start the colony.")

else:
    print(f"Area not suitable to start the colony.")
