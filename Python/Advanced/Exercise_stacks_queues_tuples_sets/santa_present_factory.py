from collections import deque

materials = deque(int(x) for x in input().split()) # pop()
magic_levels = deque(int(x) for x in input().split()) # popleft()


crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}


task = False

while materials and magic_levels:
    current_material = materials.pop() if magic_levels[0] or not materials[0] else 0
    current_magic = magic_levels.popleft() if current_material or not magic_levels[0] else 0

    product = current_material * current_magic

    if product < 0:
        materials.append(current_material + current_magic)

    elif product not in presents and product > 0:
        materials.append(current_material + 15)

    if product in presents.keys():
        crafted.append(presents[product])


if {"Doll", "Wooden Train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print(f"The presents are crafted! Merry Christmas!")

else:
    print(f"No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]