import math
number_of_tournaments = int(input())
points_beggining = int(input())
stage = ''

points_earned = 0
wins = 0

for tournaments in range(number_of_tournaments):
    current_tournament = input()
    if current_tournament == 'W':
        points_earned += 2000
        wins += 1
    elif current_tournament == 'F':
        points_earned += 1200

    elif current_tournament == 'SF':
        points_earned += 720

final_points = points_beggining + points_earned
average_points = points_earned / number_of_tournaments

percentage_of_wins = wins / number_of_tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{percentage_of_wins:.2f}%')



