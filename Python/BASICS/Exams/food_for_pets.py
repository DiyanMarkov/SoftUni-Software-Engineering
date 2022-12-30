days = int(input())
total_common_food = float(input())

total_dog = 0
total_cat = 0
days_counter = 0
total_food_eaten = 0
total_biscuits = 0

for current_food in range(1, days + 1):
    food_dog = int(input())
    food_cat = int(input())

    total_dog += food_dog
    total_cat += food_cat
    total_food_eaten += food_cat + food_dog
    days_counter += 1

    if days_counter == 3:
        biscuits = (food_dog + food_cat) * 0.10
        total_biscuits += biscuits
        days_counter = 0

percent_eaten_food = (total_food_eaten / total_common_food) * 100
percent_eaten_dog = (total_dog / total_food_eaten) * 100
percent_eaten_cat = (total_cat / total_food_eaten) * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_cat:.2f}% eaten from the cat.")