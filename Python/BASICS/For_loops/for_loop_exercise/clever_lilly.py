age = int(input())
price_laundry_machine = float(input())
price_toy = int(input())

total_toys = 0
birtday_money = 0
total_money = 0

for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        birtday_money += 10
        total_money += birtday_money - 1
    else:
        total_toys += 1

money_from_toys = total_toys * price_toy

all_money = money_from_toys + total_money

difference = abs(all_money - price_laundry_machine)

if all_money >= price_laundry_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")