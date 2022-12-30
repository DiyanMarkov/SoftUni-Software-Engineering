import math

name_series = input()
duration_of_episode = int(input())
duration_of_lunch_brake = int(input())

time_for_lunch = duration_of_lunch_brake * 0.125
time_for_relax = duration_of_lunch_brake * 0.25
left_time = duration_of_lunch_brake - (time_for_lunch + time_for_relax)

difference = abs(left_time - duration_of_episode)

if left_time >= duration_of_episode:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(difference)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(difference)} more minutes.")
