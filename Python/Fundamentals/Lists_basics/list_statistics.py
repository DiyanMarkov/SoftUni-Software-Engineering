number = int(input())
list_positive_numbers = []
list_negative_numbers = []


for current_number in range(number):
    current_number = int(input())
    if current_number >= 0:
        list_positive_numbers.append(current_number)

    elif current_number < 0:
        list_negative_numbers.append(current_number)


print(list_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {len(list_positive_numbers)}")
print(f'Sum of negatives: {sum(list_negative_numbers)}')

