number_square_meters = float(input())

price_square_meter = 7.61
discount = 0.18

price_before = (number_square_meters * price_square_meter)
discount_price = (number_square_meters * price_square_meter) * discount

final_price = abs(price_before - discount_price)


print(f'The final price is: {final_price} lv.')

print(f'The discount is: {discount_price} lv.')