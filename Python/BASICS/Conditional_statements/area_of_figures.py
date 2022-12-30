import math

type_figure = input()
side_a = float(input())

#area = 0
if type_figure == 'square':
    area = side_a * side_a
    print(f'{area:.3f}')

elif type_figure == 'rectangle':
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')

elif type_figure == 'circle':
    area = math.pi * side_a * side_a
    print(f'{area:.3f}')

elif type_figure == 'triangle':
    h = float(input())
    area = 1/2 * side_a * h
    print(f'{area:.3f}')

#print(f'{area:.3f}')     , т.е можем принта да го изкараме извън конструкцията за да не се повтаряме вътре, \
# но просто задаваме 'area' извън конструкцията и тя според фигурата вече си приема стойност, \
# принтира ни се последното