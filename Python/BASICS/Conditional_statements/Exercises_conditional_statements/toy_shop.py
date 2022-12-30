vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

numbers_toys = puzzles + talking_dolls + bears + minions + trucks


price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

price_toys_before_disc = puzzles * price_puzzle + talking_dolls * price_doll + bears * price_bear + \
             minions * price_minion + trucks * price_truck

if numbers_toys >= 50:
    price_discount = price_toys_before_disc * 0.25
    total_price = price_toys_before_disc - price_discount

else:
    total_price = price_toys_before_disc

rent = total_price * 0.10

total_sum = total_price - rent

if total_sum > vacation_price:
    print(f'Yes! {total_sum - vacation_price:.2f} lv left.')

else:
    print(f'Not enough money! {vacation_price - total_sum:.2f} lv needed.')

