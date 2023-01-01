command = input()

while command != 'Welcome!':
    length = len(command)
    if command == 'Voldemort':
        print(f"You must not speak of that name!")
        break
    if length < 5:
        print(f"{command} goes to Gryffindor.")
    elif length == 5:
        print(f"{command} goes to Slytherin.")
    elif length == 6:
        print(f"{command} goes to Ravenclaw.")
    elif length > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if command != 'Voldemort':
    print(f"Welcome to Hogwarts.")