actor = input()
beginning_points_academy = float(input())
number_of_jury = int(input())

points_actor = 0

for i in range(number_of_jury):
    name_jury = input()
    points_given = float(input())

    length = len(name_jury)
    points_actor += (length * points_given) / 2

    if beginning_points_academy + points_actor > 1250.5:
        break

total_points = beginning_points_academy + points_actor

if total_points > 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')

else:
    difference = abs(total_points - 1250.5)
    print(f'Sorry, {actor} you need {difference:.1f} more!')