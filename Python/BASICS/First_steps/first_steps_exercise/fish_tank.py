length = int(input())
width = int(input())
height = int(input())
percent_taken = int(input())

volume_tank = (length * width * height) / 1000    #cm --> dm

water_capacity = volume_tank - (volume_tank * (percent_taken/100))

print(water_capacity)

