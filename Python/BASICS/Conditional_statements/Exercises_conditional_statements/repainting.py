nilon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())

price_nilon_per_square_ft = 1.50
price_paint_per_liter = 14.50
price_thinner_per_liter = 5.00
percent_plus_paint = 110 #100 + 10% за боя, деля 110/100 =1.1 и го умножавам с боята за да получа крайния резултат с добавеното количество и умножавам по цената
price_bag = 0.40
nilon_plus = 2
percent_of_material = 30

all_nilon = (nilon_needed + nilon_plus) * price_nilon_per_square_ft
all_paint = (paint_needed * (percent_plus_paint / 100) * 14.50)
all_thinner = thinner_needed * price_thinner_per_liter

materials = all_nilon + all_paint + all_thinner + price_bag
cost_work = (materials * percent_of_material / 100) * hours_needed

total_cost = materials + cost_work

print(total_cost)



