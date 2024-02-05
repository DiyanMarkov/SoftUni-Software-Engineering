n = int(input())

odd = set()
even = set()

for i in range(1, n+1):
    name = input()
    sum = 0

    for l in name:
        sum += ord(l)

    if sum // i % 2 == 0:
        even.add(sum // i)

    else:
        odd.add(sum // i)

odd_final = 0
even_final = 0

for num in odd:
    odd_final += num

for num in even:
    even_final += num

if odd_final == even_final:
    print(', '.join([str(x) for x in odd | even]))

elif odd_final > even_final:
    print(', '.join([str(x) for x in odd.difference(even)]))

else:
    print(', '.join([str(x) for x in odd.symmetric_difference(even)]))