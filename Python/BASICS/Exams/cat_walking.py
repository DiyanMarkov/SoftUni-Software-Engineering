minutes_walking = int(input())
number_of_walks = int(input())
calories_per_day = int(input())

total_minutes = minutes_walking * number_of_walks
total_calories_burned = total_minutes * 5

half_of_eaten_calories = calories_per_day * 0.50

if total_calories_burned >= half_of_eaten_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")