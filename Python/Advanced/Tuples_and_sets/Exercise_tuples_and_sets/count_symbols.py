text = input()

occ = {}

for char in text:
    if char not in occ:
        occ[char] = 0

    occ[char] += 1


for key, value in sorted(occ.items()):
    print(f"{key}: {value} time/s", end='\n')