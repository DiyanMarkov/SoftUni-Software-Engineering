starting_points = int(input())
bonus = 0

if starting_points <= 100:
    bonus += 5       #bonus = bonus + 5

elif starting_points > 100:
    bonus += starting_points * 0.20     #bonus + starting_points * 20

elif starting_points > 1000:
    bonus += starting_points * 0.10

if starting_points % 2 == 0:
    bonus += 1

if starting_points % 10 == 5:
    bonus += 2

print(bonus)
print(starting_points + bonus)
