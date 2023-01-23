number_of_rooms = int(input())
total_free_chairs = 0
chairs_are_enough = True

for current_room in range(1, number_of_rooms + 1):
    command = input().split(' ')


    chairs = command[0]
    visitors = command[1]

    difference = len(chairs) - int(visitors)

    if len(chairs) < int(visitors):
        print(f"{abs(difference)} more chairs needed in room {current_room}")
        chairs_are_enough = False
    elif len(chairs) > int(visitors):
        total_free_chairs += difference

if chairs_are_enough:
    print(f"Game On, {total_free_chairs} free chairs left")