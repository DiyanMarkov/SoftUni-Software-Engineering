n_times = int(input())

parking_lot = set()

for i in range(n_times):
    command = input().split(', ')
    direction, plate = command

    if direction == 'IN':
        parking_lot.add(plate)
    elif direction == 'OUT':
        parking_lot.remove(plate)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print(f"Parking Lot is Empty")
