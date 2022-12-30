needed_money_vacation = float(input())
available_money = float(input())

spending_concecutive_days = False
spending_counter = 0
days = 0

while available_money < needed_money_vacation:

    if spending_counter == 5:
        spending_concecutive_days = True
        break

    action = input()
    saved_or_spend = float(input())
    days += 1

    if action == 'save':
        available_money += saved_or_spend
        spending_counter = 0

    if action == 'spend':
        spending_counter += 1
        available_money -= saved_or_spend
        if available_money < 0:
            available_money = 0

if spending_concecutive_days == True:
    print(f"You can't save the money.")
    print(days)

else:
    print(f"You saved the money for {days} days.")
