def shopping_cart(*args):

    meals = {"Soup": [], "Pizza": [], "Dessert": []}

    for arg in args:

        if arg == 'Stop':
            break

        meal = arg[0]
        product = arg[1]


        if product not in meals[meal]:

            if meal == 'Soup':
                if len(meals["Soup"]) == 3:
                    continue

            elif meal == 'Pizza':
                if len(meals['Pizza']) == 4:
                    continue

            elif meal == 'Dessert':
                if len(meals['Dessert']) == 2:
                    continue

            meals[meal].append(product)


    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for meal, products in sorted_meals:
        result += f"{meal}:\n"

        if products:

            for product in sorted(products):
                result += f" - {product}\n"

    if meals["Pizza"] == [] and meals["Dessert"] == [] and meals["Soup"] == []:
        return f"No products in the cart!"


    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))





