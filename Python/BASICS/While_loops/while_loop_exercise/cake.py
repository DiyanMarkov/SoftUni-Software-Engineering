width = int(input())
length = int(input())

all_pieces = width * length
pieces_count = 0


command = input()

there_is_more_cake = True

while command != 'STOP':

    piece_of_cake = int(command)
    pieces_count += piece_of_cake


    if all_pieces - pieces_count < 0:
        there_is_more_cake = False
        break

    command = input()

difference = abs(all_pieces - pieces_count)

if there_is_more_cake == True: #if command == 'STOP'
    print(f'{difference} pieces are left.')
else:
    print(f'No more cake left! You need {difference} pieces more.')

