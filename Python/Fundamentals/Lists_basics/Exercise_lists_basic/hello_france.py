items_list = input().split("|")
budget = float(input())
ticket_cost = 150

sold_items_value = 0

modified_prices_list = []
price_before_update = 0

for item in items_list:
    current_item = item.split('->')
    item_type = current_item[0]
    price = float(current_item[-1])
    if item_type == 'Clothes':
        if price > 50.00:
            continue
    elif item_type == 'Shoes':
        if price > 35.00:
            continue
    elif item_type == 'Accessories':
        if price > 20.50:
            continue
    if budget < price:
        continue

    budget -= price
    price_before_update += price
    modified_price_value = price + (price * 0.40)
    modified_prices_list.append(modified_price_value)
    sold_items_value += modified_price_value

final_budget = budget + sold_items_value
profit = sold_items_value - price_before_update

for price in modified_prices_list:
    print(f"{price:.2f}", end=' ')

print()
print(f'Profit: {profit:.2f}')

if final_budget >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")