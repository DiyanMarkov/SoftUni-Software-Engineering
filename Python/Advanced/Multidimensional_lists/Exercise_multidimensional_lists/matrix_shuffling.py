def is_valid_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_values(command, indices):
    if is_valid_indices(indices) and len(indices) == 4 and command == 'swap':
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(x) for x in matrix], sep="\n")

    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for x in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break

    swap_values(command, info)