def sorting_cheeses(**kwargs):
    return sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))



print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)
