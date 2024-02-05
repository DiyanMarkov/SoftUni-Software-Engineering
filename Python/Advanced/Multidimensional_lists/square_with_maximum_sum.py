rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for x in range(rows)]

submatrix = []

biggest_sum = 0
biggest_submatrix = []


for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        below_next_element = matrix[row_index + 1][col_index + 1]


        top_score = current_element + next_element
        bottom_score = below_element + below_next_element

        submatrix.append([top_score])
        submatrix.append([bottom_score])

        if top_score + bottom_score > biggest_sum:
            biggest_sum = top_score + bottom_score
            biggest_submatrix = [[current_element, next_element], [below_element, below_next_element]]


for el in biggest_submatrix:
    print(*el, sep=" ")
print(biggest_sum)
