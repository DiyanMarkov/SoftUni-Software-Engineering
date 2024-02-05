rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    numbers = [int(el) for el in input().split(", ")]

    matrix.append(numbers)


flattened = [el for ex_list in matrix for el in ex_list]

print(sum(flattened))
print(matrix)