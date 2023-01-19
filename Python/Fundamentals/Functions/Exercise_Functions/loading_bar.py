def bar_values(value):
    if value == 100:
        return f'100% Complete!\n[%%%%%%%%%%]'

    return f'{value}% [{(value // 10) * "%"}{(10 - value // 10) * "."}]\nStill loading...'


number = int(input())
print(bar_values(number))