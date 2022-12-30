days = int(input())

win_counter_day = 0
win_counter_total = 0
lose_counter_day = 0
lose_counter_total = 0
money = 0
money_day = 0

for prolonging in range(days):
    command = input()
    win_counter_day = 0
    lose_counter_day = 0
    money_day = 0

    while command != 'Finish':
        command = input()
        if command == 'win':
            win_counter_day += 1
            win_counter_total += 1
            money_day += 20
            money += 20

        elif command == 'lose':
            lose_counter_day += 1
            lose_counter_total += 1


        command = input()
    if win_counter_day > lose_counter_day:
        money += (money_day * 0.10)
        money_day = money_day + (money_day * 0.10)


if win_counter_total > lose_counter_total:
    money = money + (money * 0.20)
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")