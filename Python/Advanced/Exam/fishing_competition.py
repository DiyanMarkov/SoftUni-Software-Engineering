rows = int(input())
cols = rows

matrix = []

fisher_pos = []

for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

    if "S" in current_row:
        fisher_pos = [i, current_row.index("S")]
        matrix[fisher_pos[0]][fisher_pos[1]] = '-'


directions = {
    'up': lambda r, c: [(r - 1) % rows, c],
    'down': lambda r, c: [(r + 1) % rows, c],
    'left': lambda r, c: [r, (c - 1) % rows],
    'right': lambda r, c: [r, (c + 1) % rows],
    }

amount = 0
caught_in_whirpool = False

while True:
    command = input()

    if command == "collect the nets":
        break

    fisher_pos = directions[command](*fisher_pos)
    position = matrix[fisher_pos[0]][fisher_pos[1]]

    if position.isdigit():
        amount += int(position)
        matrix[fisher_pos[0]][fisher_pos[1]] = "-"

    if position == "W":
        caught_in_whirpool = True
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{fisher_pos[0]},{fisher_pos[1]}]")
        raise SystemExit

matrix[fisher_pos[0]][fisher_pos[1]] = "S"

if amount >= 20:
    print(f"Success! You managed to reach the quota!")

else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - amount} tons of fish more.")

if amount > 0:
    print(f"Amount of fish caught: {amount} tons.")

if not caught_in_whirpool:
    print('\n'.join([''.join(x) for x in matrix]))

#[
# ['-', '-', '-', 'S'],
# ['-', '-', '-', '-'],
# ['9', '-', '5', '-'],
# ['3', '4', '-', '-']
# ]
