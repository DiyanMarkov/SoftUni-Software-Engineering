expression = input()

stack = []
for idx in range(len(expression)):
    char = expression[idx]
    if char == '(':
        stack.append(idx)
    elif char == ')':
        last_opening_bracket_idx = stack.pop()
        sub_expression = expression[last_opening_bracket_idx:idx + 1]
        print(sub_expression)