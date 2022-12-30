day = input()

is_valid = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
is_valid_weekend = day == 'Saturday' or day == 'Sunday'

if is_valid:
    print('Working day')

elif is_valid_weekend:
    print('Weekend')

else:
    print('Error')


