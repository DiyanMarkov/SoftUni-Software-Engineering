count_times = int(input())

periodic_set = set()

for i in range(count_times):
    elements = input().split()

    for el in elements:
        periodic_set.add(el)

print(*periodic_set, sep="\n")