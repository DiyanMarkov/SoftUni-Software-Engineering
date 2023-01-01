budget = float(input())
price_1kg_flour = float(input())
price_pack_egg = price_1kg_flour * 0.75
price_liter_milk = price_1kg_flour * 1.25
price_250ml_milk = price_liter_milk / 4

price_loaf = price_1kg_flour + price_pack_egg + price_250ml_milk

colored_eggs = 0
number_of_loafs = 0

while budget > price_loaf:
    budget -= price_loaf
    number_of_loafs += 1
    colored_eggs += 3
    if number_of_loafs % 3 == 0:
        colored_eggs -= number_of_loafs - 2

money_left = budget

print(f"You made {number_of_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
