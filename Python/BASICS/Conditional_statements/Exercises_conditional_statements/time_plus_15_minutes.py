hour = int(input())
minutes = int(input())
minutes += 15

hour += minutes // 60
minutes = minutes % 60              #minutes %=

if hour > 23:
    hour = 0                     #hour -= 1   ??? но имаме лимит до 23 часа така че не е нужно, ако нямахме-->работи
if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')



