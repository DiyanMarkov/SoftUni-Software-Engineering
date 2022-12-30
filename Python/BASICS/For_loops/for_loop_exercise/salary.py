number_of_tabs = int(input())
salary = float(input())

penalty = 0

for website in range(number_of_tabs):
    website = input()
    if website == 'Facebook':
        penalty = 150
        salary -= penalty
        if salary <= 0:
            break
            print('You have lost your salary')
    elif website == 'Instagram':
        penalty = 100
        salary -= penalty
        if salary <= 0:
            break
            print('You have lost your salary')

    elif website == 'Reddit':
        penalty = 50
        salary -= penalty
        if salary <= 0:
            break
            print('You have lost your salary')

if salary <= 0:
    print('You have lost your salary')
else:
    print(int(salary))