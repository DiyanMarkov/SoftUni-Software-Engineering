parentheses = list(input())

stack = []

for char in parentheses:
    if char in "{[(":
        stack.append(char)

    if char in ")]}":
        if stack:
            if char == ")" and stack[-1] == '(':
                stack.pop()
                continue

            elif char == "]" and stack[-1] == '[':
                stack.pop()
                continue

            elif char == "}" and stack[-1] == '{':
                stack.pop()
                continue

            else:
                print('NO')
                break

        else: # if it starts with closing bracket!!!
            print('NO')
            break

else:
    print('YES')
