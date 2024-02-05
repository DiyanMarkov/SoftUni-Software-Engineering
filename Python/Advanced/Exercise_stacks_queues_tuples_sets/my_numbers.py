first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

num_times = int(input())

for i in range(num_times):
    first_command, second_command, *data = input().split()

    if first_command == 'Add':
        if second_command == 'First':
            for el in data:
                first.add(int(el))

        elif second_command == 'Second':
            for el in data:
                second.add(int(el))


    elif first_command == 'Remove':
        if second_command == 'First':
            for el in data:
                if int(el) in first:
                    first.remove(int(el))

        elif second_command == 'Second':
            for el in data:
                if int(el) in second:
                    second.remove(int(el))

    elif first_command == 'Check':
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")