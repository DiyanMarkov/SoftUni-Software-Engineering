number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = number_of_lost_fights // 2
total_swords_broken = number_of_lost_fights // 3
total_shields_broken = number_of_lost_fights // 6
total_armors_broken = total_shields_broken // 2

total_expenses = total_helmets_broken * helmet_price + total_swords_broken * sword_price + \
                 total_shields_broken * shield_price + total_armors_broken * armor_price
print(f'Gladiator expenses: {total_expenses:.2f} aureus')