def product_sum(product_name, quantity):
    total_price = None
    if product_name == 'coffee':
        total_price = quantity * 1.50
    elif product_name == 'coke':
        total_price = quantity * 1.40
    elif product_name == 'water':
        total_price = quantity * 1.00
    elif product_name == 'snacks':
        total_price = quantity * 2

    return total_price

product_name = input()
product_quantity = int(input())

print(f'{product_sum(product_name, product_quantity):.2f}')