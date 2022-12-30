
days = int(input())
food = float(input())

grams_dog = 0
grams_cat = 0
biscuits = 0


for i in range(1, days + 1):
    quantity_dog = int(input())
    quantity_cat = int(input())
    grams_dog += quantity_dog
    grams_cat += quantity_cat

    if i % 3 == 0:
        biscuits = (quantity_dog + quantity_cat) * 0.10


eaten_food = grams_dog + grams_cat
percent_eaten_food = ((grams_cat + grams_dog) / food) * 100
percent_eaten_by_dog = grams_dog / eaten_food * 100
percent_eaten_by_cat = grams_cat / eaten_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_by_cat:.2f}% eaten from the cat.")
