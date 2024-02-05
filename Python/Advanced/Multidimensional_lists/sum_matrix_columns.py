rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for i in range(rows)]
sum = 0

for col in range(cols):
    sum = 0
    for row in range(rows):
        sum += matrix[row][col]

    print(sum)