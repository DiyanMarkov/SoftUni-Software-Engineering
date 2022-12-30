number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())

number_of_eggs_first_player_counter = number_of_eggs_first_player
number_of_eggs_second_player_counter = number_of_eggs_second_player

command = input()

while command != 'End':
    if command == 'one':
        number_of_eggs_second_player_counter -= 1
    elif command == 'two':
        number_of_eggs_first_player_counter -= 1


    if number_of_eggs_first_player_counter == 0 or number_of_eggs_second_player_counter == 0:
        break

    command = input()

if number_of_eggs_first_player_counter == 0:
    print(f'Player one is out of eggs. Player two has {number_of_eggs_second_player_counter} eggs left.')
elif number_of_eggs_second_player_counter == 0:
    print(f'Player two is out of eggs. Player one has {number_of_eggs_first_player_counter} eggs left.')
elif command == 'End':
    print(f'Player one has {number_of_eggs_first_player_counter} eggs left.')

    print(f'Player two has {number_of_eggs_second_player_counter} eggs left.')
