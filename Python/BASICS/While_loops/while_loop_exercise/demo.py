goal = 10000
total_steps = 0
is_goal_reached = False


while total_steps < goal:
    action = input()

    if action == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        break

    new_action = int(action)
    total_steps += new_action

if total_steps >= 10000:
    is_goal_reached = True

difference = abs(goal - total_steps)


if is_goal_reached == True:
    print(f'Goal reached! Good job!')
    print(f'{difference} steps over the goal!')


if is_goal_reached == False:
    print(f'{difference} more steps to reach goal.')