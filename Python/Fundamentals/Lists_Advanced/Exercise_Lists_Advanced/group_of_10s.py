list_of_integers = list(map(int, input().split(', ')))

group_of_numbers = 10
counter_of_integers = 0

while counter_of_integers < len(list_of_integers):
    collected_numbers = []

    for num in list_of_integers:
        if group_of_numbers - 10 < num <= group_of_numbers:
            collected_numbers.append(num)
            counter_of_integers += 1

    print(f"Group of {group_of_numbers}'s: {collected_numbers}")
    group_of_numbers += 10