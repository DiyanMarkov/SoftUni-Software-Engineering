import random

budget = float(input(f'Budget: '))
loss_counter = 0

while budget != 0:
    bet = float(input(f'Insert your bet here: '))

    if bet > budget:
        print(f'Insufficient funds, try smaller bet!')
        continue

    budget -= bet

    list_1 = ['Cherry', 'Lemon', '7', 'Bar', 'Grape', 'Apple', 'Strawberry']
    list_2 = ['Cherry', 'Lemon', '7', 'Bar', 'Grape', 'Apple', 'Strawberry']
    list_3 = ['Cherry', 'Lemon', '7', 'Bar', 'Grape', 'Apple', 'Strawberry']

    fruit_1 = random.choice(list_1)
    fruit_2 = random.choice(list_2)
    fruit_3 = random.choice(list_3)

    print(f'{fruit_1} - {fruit_2} - {fruit_3}')

    if fruit_1 == fruit_2 == fruit_3:
        if fruit_1 == 'Cherry':
            budget += bet * 3
        elif fruit_1 == 'Lemon':
            budget += bet + bet
        elif fruit_1 == '7':
            budget += bet * 10
        elif fruit_1 == 'Grape':
            budget += bet * 2
        elif fruit_1 == 'Apple':
            budget += bet * 4
        elif fruit_1 == 'Strawberry':
            budget += bet * 6

        loss_counter = 0
        print(f'Amazing, you are so lucky! You should keep playing!')
        print(f'Balance: {budget}\n')

    elif fruit_1 == fruit_3 or fruit_1 == fruit_2 or fruit_2 == fruit_3:
        if fruit_1 or fruit_2 == "Cherry":
            budget += bet + 3
        elif fruit_1 or fruit_2 == "Lemon":
            budget += bet
        elif fruit_1 or fruit_2 == "7":
            budget += bet + 10
        elif fruit_1 or fruit_2 == "Grape":
            budget += bet + 2
        elif fruit_1 or fruit_2 == "Apple":
            budget += bet + 4
        elif fruit_1 or fruit_2 == "Strawberry":
            budget += bet + 6

        loss_counter = 0
        print(f'You have a reward! \nCheck your budget!')
        print(f'Balance: {budget}\n')

    else:
        loss_counter += 1
        print(f'You lost {bet}$ \nYou were so close... maybe next time')
        print(f'Balance: {budget}\n')

        if loss_counter > 4:
            print('You have a bad streak, maybe go for a drink and come back!')
            break
        continue


