n = int(input())

matrix = [[int(x) for x in input().split()]for i in range(n)]
primary_diagonal = [matrix[row][row] for row in range(n)]
secondary_diagonal = [matrix[row][n - row - 1] for row in range(n)]

result = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(result))