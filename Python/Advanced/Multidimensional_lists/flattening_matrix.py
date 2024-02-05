rows = int(input())

matrix = []

for _ in range(rows):
    matrix += [[int(x) for x in input().split(", ")]]


result = [el for example_list in matrix for el in example_list]
print(result)