rows = int(input())

matrix = [[int(i) for i in input().split()] for x in range(rows)]


while True:
    command, *data = input().split()
    if command == 'END':
        break

    row = data[0]
    col = data[1]
    value = data[2]

    row = int(row)
    col = int(col)
    value = int(value)

    if row not in range(0, len(matrix) -1) or col not in range(0, len(matrix) -1):
        print("Invalid coordinates")
        continue

    if command == 'Add':
        matrix[row][col] += int(value)
    elif command == 'Subtract':
        matrix[row][col] -= int(value)


[print(*row) for row in matrix]

#[
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
#           ]