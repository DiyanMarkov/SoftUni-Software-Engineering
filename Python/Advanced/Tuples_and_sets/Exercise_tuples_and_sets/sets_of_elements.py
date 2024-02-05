
first_cycle, second_cycle = [int(i) for i in input().split()]

first_set = set()
second_set = set()

for i in range(first_cycle):
    digits = int(input())
    first_set.add(digits)

for i in range(second_cycle):
    digits = int(input())
    second_set.add(digits)

print(*first_set.intersection(second_set), sep="\n")