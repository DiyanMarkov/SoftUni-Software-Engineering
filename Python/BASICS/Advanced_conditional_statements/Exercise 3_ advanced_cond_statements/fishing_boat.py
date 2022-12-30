budget_group = int(input())
season = input()
number_fishermen = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer':
    price = 4200
elif season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600


if number_fishermen <= 6:
    price = price * 0.90

elif number_fishermen >= 7 and number_fishermen <= 11:
    price = price * 0.85
else:
    price = price * 0.75

if number_fishermen % 2 == 0 and season != 'Autumn':
    price *= 0.95

difference = abs(budget_group - price)

if budget_group >= price:
    print(f'Yes! You have {difference:.2f} leva left.')

else:
    print(f'Not enough money! You need {difference:.2f} leva.')
