rows, cols = [int(i) for i in input().split()]

start = ord('a')

for row in range(start, start + rows):
    start = row
    for col in range(start, start + cols):
        print(f"{chr(row)}{chr(start)}{chr(row)}", end=" ")
        start += 1

    print()