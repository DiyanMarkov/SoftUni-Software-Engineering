type_flower = input()
number_flowers = int(input())
budget = int(input())

price_per_flower = 0
price_all = 0

if type_flower == "Roses":
    if number_flowers > 80:
        price_per_flower = 5
        price_all = number_flowers * price_per_flower * 0.90
    else:
        price_per_flower = 5
        price_all = number_flowers * price_per_flower

elif type_flower == "Dahlias":
    if number_flowers > 90:
        price_per_flower = 3.80
        price_all = number_flowers * price_per_flower * 0.85
    else:
        price_per_flower = 3.80
        price_all = number_flowers * price_per_flower


elif type_flower == "Tulips":
    if number_flowers > 80:
        price_per_flower = 2.80
        price_all = number_flowers * price_per_flower * 0.85
    else:
        price_per_flower = 2.80
        price_all = number_flowers * price_per_flower

elif type_flower == "Narcissus":
    if number_flowers < 120:
        price_per_flower = 3
        price_all = number_flowers * price_per_flower + (number_flowers * price_per_flower * 0.15)
    else:
        price_per_flower = 3
        price_all = number_flowers * price_per_flower

elif type_flower == "Gladiolus":
    if number_flowers < 80:
        price_per_flower = 2.50
        price_all = number_flowers * price_per_flower + (number_flowers * price_per_flower * 0.20)
    else:
        price_per_flower = 2.50
        price_all = number_flowers * price_per_flower

difference = abs(budget - price_all)

if budget > price_all:
    print(f'Hey, you have a great garden with {number_flowers} {type_flower} and {difference:.2f} leva left.')

else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
