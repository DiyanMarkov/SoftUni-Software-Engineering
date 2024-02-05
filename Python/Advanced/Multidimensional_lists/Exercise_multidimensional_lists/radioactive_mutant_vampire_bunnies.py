def player_position():
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'P':
                return [r, c]

def check_valid_index(row, col, player=False):
    global wins

    if 0 <= row < rows and 0 <= col < cols:
        return True

    if player:
        wins = True

def bunnies_positions():
    return [[row,col] for row in range(rows) for col in range(cols) if matrix[row][col] == 'B']


def bunnies_move(bunnies_positions):
    for row, col in bunnies_positions:
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = 'B'

def check_player_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead")


def show_results(status="won"):
    [print(*row, sep="") for row in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit

rows, cols = [int(x) for x in input().split()]
matrix = [[el for el in list(input())]for x in range(rows)]
commands = input()

wins = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


player_row, player_col = player_position()
matrix[player_row][player_col] = '.'

for command in commands:
    player_movement_row, player_movement_col = player_row + directions[command][0], player_col + directions[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col

    bunnies_move(bunnies_positions())

    if wins:
        show_results()

    check_player_alive(player_row, player_col)