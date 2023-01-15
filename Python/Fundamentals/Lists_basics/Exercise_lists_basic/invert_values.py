list_of_numbers = input().split()
opposite_list = []

for element in list_of_numbers:
    current_element = int(element)
    opposite_list.append(-current_element)

print(opposite_list)