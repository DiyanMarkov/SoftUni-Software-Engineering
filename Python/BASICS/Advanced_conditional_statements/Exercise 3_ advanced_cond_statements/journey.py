budget = float(input())
season = input()

destination = ''
type_of_holiday = ''
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.30
        type_of_holiday = 'Camp'
    if season == 'winter':
        expenses = budget * 0.70
        type_of_holiday = 'Hotel'

elif budget <= 1000:
    destination = 'Balkans'
    type_of_holiday = 'Hotel'
    if season == 'summer':
        type_of_holiday = 'Camp'
        expenses = budget * 0.40
    if season == 'winter':
        expenses = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    expenses = budget * 0.90
    type_of_holiday = 'Hotel'



print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {expenses:.2f}')

