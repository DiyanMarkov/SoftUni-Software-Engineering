number = int(input())

for current_number in range(1111, 9999 + 1):
    number_is_special = True
    current_number_as_string = str(current_number)

    if '0' in current_number_as_string:
        continue

    for current_digit in current_number_as_string:
       if number % int(current_digit) != 0:
           number_is_special = False
           break

    if number_is_special:
        print(current_number_as_string, end =' ')