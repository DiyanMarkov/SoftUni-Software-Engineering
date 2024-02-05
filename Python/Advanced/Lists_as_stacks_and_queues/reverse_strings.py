text = list(input())

result = []

while len(text) > 0:
    result.append(text.pop())

print(''.join(result), end='')