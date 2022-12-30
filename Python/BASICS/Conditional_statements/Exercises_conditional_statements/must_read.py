number_of_pages_in_book = int(input())
pages_per_hour = int(input())
days_needed = int(input())

total_time_per_book = (number_of_pages_in_book / pages_per_hour)
hours_per_day = total_time_per_book / days_needed    #total_time_per_book // days_needed  (трябва ни цяло число в отговора \
                                                      #затова или го правим с " // " или с "int" в printa

print(int(hours_per_day))
