target = int(input())

command = input()
total_money_earned = 0

while command != 'closed' or total_money_earned < target:
    if command == 'haircut':
        command = input()
        if command == 'mens':
            total_money_earned += 15

        elif command == 'ladies':
            total_money_earned += 20

        elif command == 'kids':
            total_money_earned += 10

    if command == 'color':
        command = input()

        if command == 'touch up':
            total_money_earned += 20
        if command == 'full color':
            total_money_earned += 30
    command = input()

difference = abs(total_money_earned - target)

if total_money_earned >= target:
    print(f"You have reached your target for the day!" )
else:
    print(f"Target not reached! You need {difference}lv. more.")

print(f"Earned money: {total_money_earned}lv.")