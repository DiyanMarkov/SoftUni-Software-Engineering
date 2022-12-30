width = int(input())
length = int(input())
height = int(input())

command = input()

free_space = width * length * height

there_is_more_free_space = True

while command != 'Done':

    number_of_boxes = int(command)
    free_space -= number_of_boxes

    if free_space <= 0:
        there_is_more_free_space = False
        break

    command = input()

    if number_of_boxes == 'Done':
        break

if there_is_more_free_space:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')

