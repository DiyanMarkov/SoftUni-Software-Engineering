deposited_sum = float(input())
timeframe = int(input())
annual_interest_rate = float(input())

price = deposited_sum + timeframe * ((deposited_sum * (annual_interest_rate/100) / 12))

print(price)