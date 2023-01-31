year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    if len(set_year) == len(str(year)):
        happy_year_condition = True

print(year)