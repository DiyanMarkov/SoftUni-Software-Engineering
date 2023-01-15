deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck::]
    full_list = []

    for index in range(len(left_part)):
        full_list.append(left_part[index])
        full_list.append(right_part[index])

    deck_of_cards = full_list

print(deck_of_cards)
