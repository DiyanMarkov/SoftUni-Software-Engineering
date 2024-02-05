def accommodate_new_pets(capacity, weight_limit, *args):
    pet_types = {}
    all_accomodated = True

    for pet in args:

        if capacity == 0:
            all_accomodated = False
            break

        type = pet[0]
        weight = pet[1]

        if type not in pet_types and weight <= weight_limit:
            pet_types[type] = 0

        if weight <= weight_limit:
            pet_types[type] += 1
            capacity -= 1

    result = ""

    if all_accomodated:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    else:
        result += "You did not manage to accommodate all pets!\n"

    result += "Accommodated pets:\n"

    for type, num in sorted(pet_types.items()):
        result += f"{type}: {num}\n"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))






