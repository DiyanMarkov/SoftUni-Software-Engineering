from collections import deque

bees = deque(int(x) for x in input().split()) # popleft()
nectar = deque(int(x) for x in input().split()) # pop()
operators = deque(x for x in input().split()) # popleft()

total_honey = 0

while bees and nectar:

    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_operator = operators.popleft()

        if current_operator == '/' and current_nectar == 0:
            continue

        total_honey += abs(eval(f"{current_bee} {current_operator} {current_nectar}"))

    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")