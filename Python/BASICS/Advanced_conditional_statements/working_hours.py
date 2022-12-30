hour = int(input())
day = input()

is_hour = hour <= 18 and hour >= 10
is_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'


if is_day:
    if is_hour:
        print('open')

if day == 'Sunday' or hour < 10 or hour > 18:
    print('closed')