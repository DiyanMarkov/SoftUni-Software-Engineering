n = int(input())

longest_intersection = set()

for _ in range(n):
    first, second = input().split("-")

    current_first = set()
    current_second = set()

    first_start, first_end = first.split(",")
    second_start, second_end = second.split(",")

    for f in range(int(first_start), int(first_end) + 1):
        current_first.add(int(f))

    for s in range(int(second_start), int(second_end) + 1):
        current_second.add(int(s))


    current_intersection = current_first.intersection(current_second)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")