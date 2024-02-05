
number = int(input())

stack = []


for line in range(number):
    command = input().split()

    if len(command) > 1:  # '1'/'number'
        stack.append(int(command[1]))
    elif command[0] == '2':
        if len(stack) == 0:
            continue
        stack.pop()
    elif command[0] == '3':
        if len(stack) == 0:
            continue
        print(max(stack))
    elif command[0] == '4':
        if len(stack) == 0:
            continue
        print(min(stack))


print(*stack[::-1], sep=', ')
