total_sum = 0
while True:
    current_number = input()
    if current_number == "NoMoreMoney":
        break

    current_number = float(current_number)

    if current_number < 0:
        print(f'Invalid operation!')
        break
    else:
        total_sum += current_number
        print(f'Increase: {current_number:.2f}')
print(f'Total: {total_sum:.2f}')