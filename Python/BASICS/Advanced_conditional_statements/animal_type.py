type = input()
#crocodile, tortoise, snake
is_mammal = type == 'dog'
is_reptile = type == 'crocodile' or type == 'tortoise' or type == 'snake'

if is_mammal:
    print('mammal')

elif is_reptile:
    print('reptile')

else:
    print('unknown')