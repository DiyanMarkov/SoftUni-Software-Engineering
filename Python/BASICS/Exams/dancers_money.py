dancers = int(input())
points = float(input())
season = input()
place = input()

if place == 'Bulgaria':
    prize = dancers * points
    if season == 'summer':
        prize = prize - (prize * 0.05)

    elif season == 'winter':
        prize = prize - (prize * 0.08)

elif place == 'Abroad':
    money = dancers * points
    prize = money + money * 0.50

    if season == 'summer':
        prize = prize - (prize * 0.10)

    elif season == 'winter':
        prize = prize - (prize * 0.15)

charity_money = prize * 0.75
money_left = prize - charity_money
money_per_dancer = money_left / dancers

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")