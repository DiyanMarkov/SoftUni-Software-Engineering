price_party = float(input())
love_letter = int(input())
roses = int(input())
key_holders = int(input())
caricatures = int(input())
luck_suprise = int(input())


total_love_letter = love_letter * 0.60
total_roses = roses * 7.20
total_key_holders = key_holders * 3.60
total_caricatures = caricatures * 18.20
total_luck_suprise = luck_suprise * 22

total_won = total_love_letter + total_roses + total_key_holders + total_caricatures + total_luck_suprise
number_sold = love_letter + roses + key_holders + caricatures + luck_suprise

if number_sold > 25:
    total_won = total_won * 0.65

total_won = total_won - (total_won * 0.10)

difference = abs(total_won - price_party)

if total_won >= price_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")