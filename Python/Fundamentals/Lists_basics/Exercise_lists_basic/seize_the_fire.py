all_cells_values = input().split('#')
water = int(input())

total_effort = 0
total_fire = 0
valid_values = []

for cell in all_cells_values:
    current_cell = cell.split(' = ')
    type_of_fire = current_cell[0]
    range = int(current_cell[-1])
    if type_of_fire == 'High':
        if not 81 <= range <= 125:
            continue
    elif type_of_fire == 'Medium':
        if not 51 <= range <= 80:
            continue
    elif type_of_fire == 'Low':
        if not 1 <= range <= 50:
            continue
    if water < range:
        continue
    water -= range
    total_effort += range * 0.25
    valid_values.append(range)
    total_fire += range

print(f'Cells:')
for each_cell in valid_values:
    print(f' - {each_cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')

