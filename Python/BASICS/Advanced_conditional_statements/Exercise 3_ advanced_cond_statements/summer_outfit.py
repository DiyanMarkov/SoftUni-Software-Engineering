degrees = int(input())
time_of_day = input()

Outfit = ''
Shoes = ''

if 10 <= degrees <= 18:
    if time_of_day == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    if time_of_day == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    if time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

elif 18 < degrees <= 24:
    if time_of_day == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    if time_of_day == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    if time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

elif degrees >= 25:
    if time_of_day == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    if time_of_day == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    if time_of_day == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {degrees:.2f} degrees, get your {Outfit} and {Shoes}")
