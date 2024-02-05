
my_rack = [int(x) for x in input().split()]
capacity = int(input())
n = capacity
count_racks = 1

while my_rack:
    if my_rack[-1] <= n:
        current_cloth = my_rack.pop()
        n -= current_cloth

    else:
        count_racks += 1
        current_cloth = my_rack.pop()
        n = capacity - current_cloth

print(count_racks)