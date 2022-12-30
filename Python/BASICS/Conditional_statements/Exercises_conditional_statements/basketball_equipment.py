annual_tax = int(input())
sneakers_price = annual_tax - (annual_tax * 40/100)   # * 0.60
outfit_price = sneakers_price - (sneakers_price * 20 / 100) # * 0.80
ball_price = outfit_price / 4  # * 1 / 4
accesories_price = ball_price / 5  # * 1 / 5

total_price = annual_tax + sneakers_price + outfit_price + ball_price + accesories_price

print(total_price)