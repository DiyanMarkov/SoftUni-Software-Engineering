number = int(input())

first = str(number)[2]
second = str(number)[1]
third = str(number)[0]

for i in range(int(first) + 1):
    if int(i) <= 0:
        continue
    for j in range(int(second) + 1):
        if int(j) <= 0:
            continue
        for k in range(int(third) + 1):
            if int(k) <= 0:
                continue

            result = i * j * k
            print(f'{i} * {j} * {k} = {result};')