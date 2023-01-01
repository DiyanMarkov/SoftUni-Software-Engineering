british_pounds = int(input())
exchange_rate = 1.31
us_dollars = british_pounds * exchange_rate

print(f'{us_dollars:.3f}')

# from forex_python.converter import CurrencyRates
#
# amount_GBP = int(input())
# c = CurrencyRates()
# current_rate = c.get_rate('GBP', 'USD')
# amount_USD = amount_GBP * current_rate
#
# print(f'{amount_USD:.3f}')
