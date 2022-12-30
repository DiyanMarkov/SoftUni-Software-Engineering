number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegan_menus = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegan_menu = 8.15
delivery = 2.50

price_menus = number_chicken_menus * price_chicken_menu + number_fish_menus * price_fish_menu + number_vegan_menus * price_vegan_menu
dessert = price_menus * 0.20

total_price = price_menus + dessert + delivery

print(total_price)