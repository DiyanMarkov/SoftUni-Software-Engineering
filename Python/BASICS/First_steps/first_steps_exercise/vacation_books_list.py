pages_current_book = int(input())
pages_per_hour = int(input())
number_of_days_needed_to_finish_book = int(input())

all_hours = pages_current_book / pages_per_hour
hours_per_day = all_hours / number_of_days_needed_to_finish_book
print(int(hours_per_day))