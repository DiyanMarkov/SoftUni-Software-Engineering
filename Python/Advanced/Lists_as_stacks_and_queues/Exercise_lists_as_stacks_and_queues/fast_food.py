from collections import deque

quantity_food = int(input())
food = deque([int(x) for x in input().split()])

print(max(food))

for i in range(len(food)):
    if quantity_food <= food[0]:
        break
    quantity_food -= int(food[0])
    food.popleft()


if len(food) > 0:
    #result = ''
    #for i in range(len(food)):
        #result += str(food.popleft()) + ' '
    print(f"Orders left:", *food, sep=' ')
else:
    print('Orders complete')

#348
#20 54 30 16 7 9
