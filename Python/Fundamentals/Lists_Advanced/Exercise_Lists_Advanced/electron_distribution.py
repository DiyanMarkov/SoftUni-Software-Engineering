electrons = int(input())
shells = []
n = 0
i = 0
while electrons >= 0:
    if electrons <= 0:
        break

    electrones_excluded = 2 * (n + 1) ** 2
    if electrons < electrones_excluded:
        shells.insert(n, electrons)
        break
    shells.insert(0 + i, electrones_excluded)
    i += 1
    n += 1
    electrons -= electrones_excluded

print(shells)