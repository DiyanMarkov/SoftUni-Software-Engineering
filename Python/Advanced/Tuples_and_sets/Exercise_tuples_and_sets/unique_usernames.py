names_count = int(input())

set_names = set()

for i in range(names_count):
    name = input()

    set_names.add(name)

print('\n'.join(set_names))


