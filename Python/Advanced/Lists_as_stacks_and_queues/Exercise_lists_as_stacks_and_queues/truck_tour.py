from collections import deque

n = int(input())

index = 0

tank = 0
q = deque([int(x) for x in input().split()] for _ in range(n))

pumps_copy = q.copy()

while pumps_copy:
    amount, distance = pumps_copy[0]

    tank += amount

    if tank >= distance:
        pumps_copy.popleft()
        tank -= distance
        continue

    else:
        index += 1
        tank = 0
        current_pump = q.popleft()
        q.append(current_pump)
        pumps_copy = q.copy()

print(index)