integer_list = input().split(', ')
count_of_beggars = int(input())
full_list_integers = []
temporary_storage_value = 0

final_list = []
counter_of_index = 0

for element in integer_list:
    current_element = int(element)
    full_list_integers.append(current_element)

while counter_of_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(counter_of_index, len(full_list_integers), count_of_beggars):
        sum_of_current_beggar += full_list_integers[current_index]

    counter_of_index += 1
    final_list.append(sum_of_current_beggar)

print(final_list)


