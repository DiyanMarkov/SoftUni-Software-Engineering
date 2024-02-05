from collections import deque

portions = deque([int(x) for x in input().split(", ")]) # pop()
staminas = deque([int(x) for x in input().split(", ")]) # popleft()

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70),
])


conquered = []

while portions and staminas and len(conquered) < 5:

    food = portions.pop()
    stamina = staminas.popleft()
    next_peak = peaks.popleft()

    sum = food + stamina

    if sum >= next_peak[1]:
        conquered.append(next_peak[0])

    else:
        peaks.appendleft(next_peak)


if not peaks:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print(f"Conquered peaks:")

    for peak in conquered:
        print(peak)