budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_cost = int(input())




if number_of_nights > 7:
    price_per_night = price_per_night * 0.95


total_price = (number_of_nights * price_per_night) + budget * (percent_additional_cost / 100)

difference = abs(budget - total_price)

if budget > total_price:
    print(f'Ivanovi will be left with {difference:.2f} leva after vacation.')
else:
    print(f'"{difference:.2f} leva needed."')

