destination = input()

while destination != 'End':
    price_trip = float(input())
    sum_for_trip = 0
    while sum_for_trip < price_trip:
        current_price = float(input())
        sum_for_trip += current_price

    print(f'Going to {destination}!')

    destination = input()




