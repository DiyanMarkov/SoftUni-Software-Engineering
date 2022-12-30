number_packages_pens = int(input())
number_packages_markers = int(input())
liters_liquid_cleaner = int(input())
discount_percentage = int(input())

price_per_package_pens = 5.80
price_per_package_markers = 7.20
price_per_liter_liquid_cleaner = 1.20

total_price_pens = number_packages_pens * price_per_package_pens
total_price_markers = number_packages_markers * price_per_package_markers
total_price_liters_liquid_cleaner = liters_liquid_cleaner * price_per_liter_liquid_cleaner

total_cost_before_discount = total_price_markers + total_price_pens + total_price_liters_liquid_cleaner
total_cost_with_discount = total_cost_before_discount - (total_cost_before_discount * (discount_percentage / 100))

print(total_cost_with_discount)