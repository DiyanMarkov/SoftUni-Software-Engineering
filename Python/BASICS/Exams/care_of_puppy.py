bought_food_kg = int(input())
bought_food_gr = bought_food_kg * 1000

command = input()
eaten_food = 0

while command != 'Adopted':
    command = int(command)
    eaten_food += command



    command = input()

difference = abs(bought_food_gr - eaten_food)

if bought_food_gr >= eaten_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more." )