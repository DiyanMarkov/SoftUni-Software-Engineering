month = input()
number_of_stays  = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if number_of_stays > 7 and number_of_stays <= 14:
        studio = 50 * 0.95

    if number_of_stays > 14:
        studio = 50 * 0.70
        apartment = 65 * 0.90

if month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70

    if number_of_stays > 14:
        studio = 75.20 * 0.80
        apartment = 68.70 * 0.90

if month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if number_of_stays > 14:
        apartment = 77 * 0.90

cost_apartment = apartment * number_of_stays
cost_studio = studio * number_of_stays

print(f'Apartment: {cost_apartment:.2f} lv.')
print(f'Studio: {cost_studio:.2f} lv.')