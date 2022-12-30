fruit = input()
size = input()
number_of_sets = int(input())

if size == 'small':

    if fruit == 'Watermelon':
        price_set = 56 * 2
        total = number_of_sets * price_set
    elif fruit == 'Mango':
        price_set = 36.66 * 2
        total = number_of_sets * price_set
    elif fruit == 'Pineapple':
        price_set = 42.10 * 2
        total = number_of_sets * price_set
    elif fruit == 'Raspberry':
        price_set = 20 * 2
        total = number_of_sets * price_set

if size == 'big':

    if fruit == 'Watermelon':
        price_set = 28.70 * 5
        total = number_of_sets * price_set
    elif fruit == 'Mango':
        price_set = 19.60 * 5
        total = number_of_sets * price_set
    elif fruit == 'Pineapple':
        price_set = 24.80 * 5
        total = number_of_sets * price_set
    elif fruit == 'Raspberry':
        price_set = 15.20 * 5
        total = number_of_sets * price_set

if total >= 400 and total <= 1000:
    total *= 0.85
if total > 1000:
    total *= 0.50

print(f'{total:.2f} lv.')


