budget_film = float(input())
number_of_extras = int(input())
price_outfit_per_extra = float(input())

price_all_outfit = number_of_extras * price_outfit_per_extra

decor = budget_film * 0.10

needed_money = decor + price_all_outfit
difference = abs(needed_money - budget_film)   # слагам абсолютната стойност от разликата между нужната сума и това \
                                            #с което разполагаме като бюджет за да не се притеснявам кое от кое \
                                            #да вадя (да не смятам директно в принта и да не обърккам!!!)

if number_of_extras > 150:
    price_all_outfit -= price_all_outfit * 0.10   #price_all_outfit *= 0.90

if decor + price_all_outfit > budget_film:
    print('Not enough money!')
    print(f'Wingard needs {difference: .2f} leva more.')

if decor + price_all_outfit <= budget_film:
    print('Action!')
    print(f'Wingard starts filming with {difference: .2f} leva left.')



