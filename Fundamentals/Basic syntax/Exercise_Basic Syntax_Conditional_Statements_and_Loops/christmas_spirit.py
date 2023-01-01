quantity_of_decorations = int(input())
days_until_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

budget_needed = 0
spirit_points = 0

for current_day in range(1, days_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2

    if current_day % 2 == 0:
        budget_needed += quantity_of_decorations * ornament_set
        spirit_points += 5
    if current_day % 3 == 0:
        budget_needed += quantity_of_decorations * (tree_skirt + tree_garland)
        spirit_points += 13
    if current_day % 5 == 0:
        budget_needed += quantity_of_decorations * tree_lights
        spirit_points += 17
        if current_day % 3 == 0:
            spirit_points += 30

    if current_day % 10 == 0:
        spirit_points -= 20
        budget_needed += tree_skirt + tree_garland + tree_lights

if current_day % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {budget_needed}")
print(f"Total spirit: {spirit_points}")