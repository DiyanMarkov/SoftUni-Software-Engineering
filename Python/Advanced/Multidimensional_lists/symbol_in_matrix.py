rows = int(input())

matrix = [[x for x in list(input())] for x in range(rows)]

is_found = True

symbol = input()
for i in range(rows):
    for j in range(rows):
        if matrix[i][j] != symbol:
            is_found = False
            continue
        print(f'{i, j}')
        is_found = True
        exit()


if is_found == False:
    print(f"{symbol} does not occur in the matrix")

#[
# ['A', 'B', 'C'],
# ['D', 'E', 'F'],
# ['X', '!', '@'],
#                   ]

