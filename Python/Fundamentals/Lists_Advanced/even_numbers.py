list_of_numbers = list(map(int, input().split(', ')))
indices = [i for i in range(len(list_of_numbers)) if list_of_numbers[i] % 2 == 0]
print(indices)