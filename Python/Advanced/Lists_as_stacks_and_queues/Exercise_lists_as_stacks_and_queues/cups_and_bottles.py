from collections import deque

cups = deque([int(x) for x in input().split()]) # appendleft()
bottles = deque([int(x) for x in input().split()]) # pop()

wasted_water = 0

'''get the bottles and fill the cups'''

while cups and bottles:

    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup

    else:
        cups.appendleft(current_cup)
        current_cup -= current_bottle

        while current_cup > 0:

            next_bottle = bottles.pop()
            if next_bottle >= current_cup:
                wasted_water += next_bottle - current_cup
                cups.popleft()
                break

            else:
                current_cup -= next_bottle


if not cups:
    print(f"Bottles:", *bottles)

else:
    print(f"Cups:", *cups)


print(f"Wasted litters of water: {wasted_water}")