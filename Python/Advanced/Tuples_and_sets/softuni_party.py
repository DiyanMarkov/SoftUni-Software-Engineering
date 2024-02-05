n_times = int(input())

vip = set()
all_list = set()
guests_who_came = set()

for i in range(n_times):
    code = input()
    if code[0].isdigit():
        vip.add(code)
        all_list.add(code)
    else:
        all_list.add(code)


while True:
    guest = input()
    if guest == 'END':
        break
    guests_who_came.add(guest)


result = all_list.difference(guests_who_came)
print(len(result))
result = sorted(result)

print(*result, sep='\n')
