budget_movie = float(input())
destination = input()
season = input()
days = int(input())

if season == 'Winter':
    if destination == 'Dubai':
        price_per_day = 45000
        price_before_tax = price_per_day * days
        total_price = price_before_tax * 0.70
    elif destination == 'Sofia':
        price_per_day = 17000
        price_before_tax = price_per_day * days
        total_price = price_before_tax + price_before_tax * 0.25
    elif destination == 'London':
        price_per_day = 24000
        total_price = price_per_day * days

if season == 'Summer':
    if destination == 'Dubai':
        price_per_day = 40000
        price_before_tax = price_per_day * days
        total_price = price_before_tax * 0.70
    elif destination == 'Sofia':
        price_per_day = 12500
        price_before_tax = price_per_day * days
        total_price = price_before_tax + price_before_tax * 0.25
    elif destination == 'London':
        price_per_day = 20250
        total_price = price_per_day * days

difference = abs(budget_movie - total_price)

if budget_movie > total_price:
    print(f'The budget for the movie is enough! We have {difference:.2f} leva left!')
else:
    print(f'The director needs {difference:.2f} leva more!')