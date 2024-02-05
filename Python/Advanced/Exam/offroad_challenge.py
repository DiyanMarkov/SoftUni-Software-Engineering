from collections import deque

fuels = deque([int(x) for x in input().split()]) #pop()
consumptions = deque([int(x) for x in input().split()]) #popleft()
needed_fuel = deque([int(x) for x in input().split()])

index = 0
not_enough_fuel = False

reached = []

while fuels and consumptions:
    fuel = fuels.pop()
    consumption = consumptions.popleft()

    result = abs(fuel - consumption)
    next_needed_fuel = needed_fuel.popleft()

    index += 1

    if result >= next_needed_fuel:
        reached.append(f"Altitude {index}")
        print(f"John has reached: Altitude {index}")

    elif result < next_needed_fuel:
        not_enough_fuel = True
        print(f"John did not reach: Altitude {index}")
        break

    if not fuels and not consumptions:
        print(f"John has reached all the altitudes and managed to reach the top!")
        raise SystemExit

if not_enough_fuel == True and len(reached) != 0:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached)}")

elif not_enough_fuel == True and len(reached) == 0:
    print(f"John failed to reach the top.")
    print(f"John didn't reach any altitude.")