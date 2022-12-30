deposited_sum = float(input())
deposit_term_months = int(input())
annual_interest_rate = float(input())

interest_rate_per_month = ((deposited_sum * annual_interest_rate) / 100) / 12
accumulated_interest = deposit_term_months * interest_rate_per_month
total_sum = deposited_sum + accumulated_interest


#end_sum = deposited_sum + deposit_term_months * ((deposited_sum * annual_interest_rate/100) / 12)
# НАКРАТКО ТАКА може

print(total_sum)
