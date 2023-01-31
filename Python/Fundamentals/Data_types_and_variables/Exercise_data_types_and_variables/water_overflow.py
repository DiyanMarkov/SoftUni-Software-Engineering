number_of_lines = int(input())
water_tank_capacity = 255
poured_liters = 0

for line in range(number_of_lines):
    current_line = int(input())
    poured_liters += current_line
    if water_tank_capacity < poured_liters:
        print(f"Insufficient capacity!")
        poured_liters -= current_line
        continue
if abs(poured_liters - water_tank_capacity) < 0:
    print('0')
else:
    print(poured_liters)
