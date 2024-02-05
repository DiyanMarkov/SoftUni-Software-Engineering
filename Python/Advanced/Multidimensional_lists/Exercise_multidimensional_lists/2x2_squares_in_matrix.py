rows, cols = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for i in range(rows)]

square_matrices = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        below_element = matrix[row + 1][col]
        below_next_element = matrix[row + 1][col + 1]

        if current_element == next_element == below_element == below_next_element:
            square_matrices += 1


print(square_matrices)
#[
# ['A', 'B', 'B', 'D'],
# ['E', 'B', 'B', 'B'],
# ['I', 'J', 'B', 'B']
#                        ]