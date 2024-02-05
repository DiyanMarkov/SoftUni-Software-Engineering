from collections import deque
from copy import copy

price_bullet = int(input())
number_of_bullets = int(input())

size_barrel = copy(number_of_bullets)
bullets_fired = 0

bullets = deque([int(x) for x in input().split()])  # pop()
locks = deque([int(x) for x in input().split()])     #popleft

reward = int(input())

while bullets and locks:

    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print(f"Bang!")

    else:
        locks.appendleft(current_lock)
        print(f"Ping!")

    size_barrel -= 1
    bullets_fired += 1

    if bullets and size_barrel == 0:
        size_barrel = number_of_bullets if len(bullets) >= number_of_bullets else len(bullets)
        print(f'Reloading!')

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${reward - (bullets_fired * price_bullet)}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")