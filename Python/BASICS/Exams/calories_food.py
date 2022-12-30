percent_fats = int(input()) / 100
percent_protein = int(input()) / 100
percent_carbs = int(input()) / 100
total_calories = int(input())
percent_water = int(input()) / 100

total_fats = (percent_fats * total_calories) / 9
total_protein = (percent_protein * total_calories) / 4
total_carbs = (percent_carbs * total_calories) / 4

total_food = total_fats + total_protein + total_carbs
calories_per_gram_food = total_calories / total_food

how_much_water = calories_per_gram_food * percent_water


result = calories_per_gram_food - how_much_water
print(f'{result:.4f}')

