days = int(input())
type_of_room = input()
review = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

price = 0
nights = days - 1

if type_of_room == 'room for one person':
    price = nights * room_for_one_person

if days < 10:
    if type_of_room == 'apartment':
        price = nights * apartment * 0.70

    if type_of_room == 'president apartment':
        price = nights * president_apartment * 0.90

if days >= 10 and days <= 15:
    if type_of_room == 'apartment':
        price = nights * apartment * 0.65

    if type_of_room == 'president apartment':
        price = nights * president_apartment * 0.85

if days > 15:
    if type_of_room == 'apartment':
        price = nights * apartment * 0.50

    if type_of_room == 'president apartment':
        price = nights * president_apartment * 0.80

if review == 'positive':
    all_cost = price + (price * 0.25)

if review == 'negative':
    all_cost = price - (price * 0.10)

print(f'{all_cost:.2f}')

