chicken = int(input())
fish = int(input())
vegan = int(input())

price_chicken = 10.35
price_fish = 12.40
price_vegan = 8.15
delivery = 2.50
dessert_percent = 20

cost_food = chicken * price_chicken + fish * price_fish + vegan * price_vegan

dessert = cost_food * (dessert_percent / 100)

total_price = cost_food + dessert + delivery

print(total_price)

