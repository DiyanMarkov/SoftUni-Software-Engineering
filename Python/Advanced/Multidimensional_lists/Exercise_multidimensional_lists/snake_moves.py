from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

matrix = []

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if row % 2 == 0:
        matrix = [word_copy.popleft() for x in range(cols)]
    else:
        matrix = [word_copy.popleft() for x in range(cols)][::-1]

    print(*matrix, sep="")