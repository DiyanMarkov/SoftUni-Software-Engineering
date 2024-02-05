rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for x in range(rows)]

submatrix = []

biggest_sum = float('-inf')
biggest_submatrix = []


for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        top_last_element = matrix[row_index][col_index + 2]


        middle_element = matrix[row_index + 1][col_index]
        middle_next_element = matrix[row_index + 1][col_index + 1]
        middle_last_element = matrix[row_index + 1][col_index + 2]

        bottom_element = matrix[row_index + 2][col_index]
        bottom_next_element = matrix[row_index + 2][col_index + 1]
        bottom_last_element = matrix[row_index + 2][col_index + 2]


        top_score = current_element + next_element + top_last_element
        middle_score = middle_element + middle_next_element + middle_last_element
        bottom_score = bottom_element + bottom_next_element + bottom_last_element


        if top_score + middle_score + bottom_score  > biggest_sum:
            biggest_sum = top_score + middle_score + bottom_score
            biggest_submatrix = [[current_element, next_element, top_last_element],
                                 [middle_element, middle_next_element, middle_last_element],
                                 [bottom_element, bottom_next_element, bottom_last_element]]


print(f"Sum = {biggest_sum}")
for el in biggest_submatrix:
    print(*el, sep=" ")