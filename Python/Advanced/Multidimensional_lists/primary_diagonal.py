rows = int(input())

matrix = []

for row in range(rows):
    numbers = [int(el) for el in input().split()]

    matrix.append(numbers)

result = 0

for i in range(rows):
    for j in range(rows):
        if j != i:
            continue
        result += matrix[i][j]

print(result)


# [
#   [11, 2, 4],
#   [4, 5, 6],
#   [10, 8, -12]]
# ]
