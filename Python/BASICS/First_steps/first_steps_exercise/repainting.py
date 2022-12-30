nilon = int(input())
paint = int(input())
paint_thinner = int(input())
hours_work = int(input())

bags = 0.40

price_nilon = 1.50
price_paint = 14.50
price_thinner = 5


expenses_materials = (nilon + 2) * price_nilon + (paint + paint * 0.10) * price_paint + paint_thinner * price_thinner + bags
price_workers_hourly = expenses_materials * 0.30

total_sum = price_workers_hourly * hours_work + expenses_materials

print(total_sum)