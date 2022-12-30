price_strawberry = float(input())
quantity_banana = float(input())
quantity_orange = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())

price_raspberry = price_strawberry * 0.5
price_orange = price_raspberry * 0.6
price_banana = price_raspberry * 0.2

total_strawberry = quantity_strawberry * price_strawberry
total_banana = quantity_banana * price_banana
total_orange = quantity_orange * price_orange
total_raspberry = quantity_raspberry * price_raspberry

total_money_needed = total_strawberry + total_banana + total_orange + total_raspberry

print(f'{total_money_needed:.2f}')
