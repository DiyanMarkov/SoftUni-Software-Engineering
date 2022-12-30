pen_packages = int(input())
sharpies_packages = int(input())
chalkboard_cleaner = int(input())
percent_discount = int(input())

price_pens = 5.80
price_sharpies = 7.20
price_cleaner = 1.20

price_before_discount = pen_packages * price_pens + sharpies_packages * price_sharpies + chalkboard_cleaner * price_cleaner
discount_price = (pen_packages * price_pens + sharpies_packages * price_sharpies + chalkboard_cleaner * price_cleaner) * (percent_discount / 100)

end_price = price_before_discount - discount_price

print(end_price)