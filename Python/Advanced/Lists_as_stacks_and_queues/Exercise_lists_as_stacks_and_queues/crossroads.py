from collections import deque
from copy import deepcopy

duration_green = int(input())
free_window = int(input())

green_copy = deepcopy(duration_green)

total_passed = 0

q = deque()

info = input()

while info != "END":
    if info != "green":
        q.append(info)
    else:
        duration_green = green_copy

        while duration_green > 0 and q:
            current_car = q.popleft()

            time = duration_green + free_window

            if len(current_car) > time:
                print(f"A crash happened!")
                print(f"{current_car} was hit at {current_car[duration_green + free_window]}.")

                raise SystemExit

            duration_green -= len(current_car)
            total_passed += 1

    info = input()

print("Everyone is safe.")
print(f"{total_passed} total cars passed the crossroads.")