#плод - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
#ден от седмицата - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
#количество (реално число).

fruit = input()
day = input()
quantity = float(input())

price = 0

is_valid = True

price_fruit = quantity * price

is_fruit = fruit == 'banana' or fruit == 'apple' or fruit == 'kiwi' or fruit == 'grapefruit' or fruit == 'orange' \
           or fruit == 'pineapple' or fruit == 'grapes'

is_work_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'

is_weekend_day = day == 'Saturday' or day == 'Sunday'

if is_fruit:
    if is_work_day:
        if fruit == 'banana':
            price = 2.50
        elif fruit == 'apple':
            price = 1.20
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.70
        elif fruit == 'pineapple':
            price = 5.50
        elif fruit == 'grapes':
            price = 3.85
        price_fruit = quantity * price
    else:
        is_valid = False

    if is_weekend_day:
        if fruit == 'banana':
            price = 2.70
        elif fruit == 'apple':
            price = 1.25
        elif fruit == 'orange':
            price = 0.90
        elif fruit == 'grapefruit':
            price = 1.60
        elif fruit == 'kiwi':
            price = 3
        elif fruit == 'pineapple':
            price = 5.60
        elif fruit == 'grapes':
            price = 4.20
        price_fruit = quantity * price
    else:
        is_valid = False

else:
    is_valid = False

if (is_fruit and is_weekend_day) or (is_fruit and is_work_day):
    print(f'{price_fruit:.2f}')
else:
    print('error')
