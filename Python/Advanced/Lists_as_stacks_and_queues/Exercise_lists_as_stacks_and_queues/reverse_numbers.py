numbers = input().split()

reversed = []

for i in range(len(numbers)):
    current_number = numbers.pop()
    reversed.append(current_number)

print(*reversed)