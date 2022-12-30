budget = float(input())
num_videocards = int(input())
num_processors = int(input())
num_ram = int(input())


price_per_videocard = 250

total_video = num_videocards * price_per_videocard

price_per_processor = total_video * 0.35

total_processors = num_processors * price_per_processor

price_per_ram = total_video * 0.10

total_ram = num_ram * price_per_ram

total_parts = total_video + total_processors + total_ram

if num_videocards > num_processors:
    discount = total_parts * 0.15
    total_parts -= discount

difference = abs(budget - total_parts)

if budget > total_parts:
    print(f'You have {difference:.2f} leva left!')

else:
    print(f'Not enough money! You need {difference:.2f} leva more!')



